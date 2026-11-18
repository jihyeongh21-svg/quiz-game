"""QuizGame 클래스: 메뉴, 퀴즈 목록, 최고 점수, 저장/불러오기."""

import json
import os
import signal

from quiz import Quiz

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")


class QuizGame:
    """메뉴, 퀴즈 목록, 최고 점수를 관리하는 게임 본체."""

    def __init__(self):
        self.quizzes = self.default_quizzes()
        self.best_score = None
        self.load_state()

    @staticmethod
    def default_quizzes():
        """주제: 파이썬 기초 문법 퀴즈 6개."""
        return [
            Quiz("Python의 창시자는?", ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"], 1),
            Quiz("리스트를 나타내는 기호는?", ["()", "[]", "{}", "<>"], 2),
            Quiz("정수 자료형의 이름은?", ["str", "bool", "int", "dict"], 3),
            Quiz("반복 횟수가 정해진 반복에 주로 쓰는 문법은?", ["if", "for", "def", "try"], 2),
            Quiz("함수를 정의할 때 쓰는 키워드는?", ["func", "lambda", "define", "def"], 4),
            Quiz("키-값 쌍으로 데이터를 저장하는 자료형은?", ["dict", "list", "tuple", "set"], 1),
        ]

    # ----- 저장 / 불러오기 -----
    def reset_to_default(self):
        self.quizzes = self.default_quizzes()
        self.best_score = None

    def load_state(self):
        """state.json을 읽는다. 없으면 기본값, 손상되면 기본값으로 복구."""
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
            best = data["best_score"]
            if best is not None and (not isinstance(best, int) or isinstance(best, bool) or best < 0):
                raise ValueError("잘못된 최고 점수")
        except FileNotFoundError:
            return  # 첫 실행: 기본 퀴즈 사용
        except (json.JSONDecodeError, KeyError, TypeError, ValueError, UnicodeDecodeError):
            print("데이터 파일이 손상되어 기본 퀴즈로 초기화합니다.")
            self.backup_corrupt_file()
            self.reset_to_default()
            self.save_state()
            return
        except OSError as e:
            print(f"데이터 파일을 읽을 수 없어 기본 퀴즈를 사용합니다. ({e})")
            return
        self.quizzes, self.best_score = quizzes, best

    def backup_corrupt_file(self):
        """손상된 파일을 state.json.corrupt로 보존해 사용자가 복구할 수 있게 한다."""
        backup = STATE_FILE + ".corrupt"
        try:
            os.replace(STATE_FILE, backup)
            print(f"손상된 원본은 '{os.path.basename(backup)}'로 보관했습니다.")
        except OSError as e:
            print(f"손상된 파일을 백업하지 못했습니다: {e}")

    def save_state(self):
        data = {"quizzes": [q.to_dict() for q in self.quizzes], "best_score": self.best_score}
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"저장에 실패했습니다: {e}")

    # ----- 입력 처리 -----
    def read_int(self, prompt, low, high):
        """low~high 사이 정수를 입력받는다. 잘못된 입력이면 재입력."""
        while True:
            raw = input(prompt).strip()
            if not raw:
                print("입력이 비어 있습니다. 다시 입력해 주세요.")
                continue
            try:
                value = int(raw)
            except ValueError:
                print("숫자만 입력해 주세요.")
                continue
            if not low <= value <= high:
                print(f"{low}~{high} 사이의 숫자를 입력해 주세요.")
                continue
            return value

    def read_text(self, prompt):
        """빈 문자열이 아닌 텍스트를 입력받는다."""
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("입력이 비어 있습니다. 다시 입력해 주세요.")

    # ----- 기능 -----
    def show_menu(self):
        print("\n===== 파이썬 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        score = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            if quiz.is_correct(self.read_int("정답 번호(1~4): ", 1, 4)):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")
        print(f"\n결과: {len(self.quizzes)}문제 중 {score}문제 정답")
        self.update_best_score(score)

    def update_best_score(self, score):
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("최고 점수를 갱신했습니다!")
            self.save_state()

    def add_quiz(self):
        question = self.read_text("문제: ")
        choices = [self.read_text(f"선택지 {i}: ") for i in range(1, 5)]
        answer = self.read_int("정답 번호(1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n--- 퀴즈 목록 (총 {len(self.quizzes)}개) ---")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")

    @staticmethod
    def handle_sigterm(signum, frame):
        """SIGTERM(종료 요청)을 KeyboardInterrupt와 같은 안전 종료 경로로 보낸다."""
        raise KeyboardInterrupt

    def run(self):
        signal.signal(signal.SIGTERM, self.handle_sigterm)
        actions = {1: self.play, 2: self.add_quiz, 3: self.list_quizzes, 4: self.show_best_score}
        try:
            while True:
                self.show_menu()
                choice = self.read_int("선택: ", 1, 5)
                if choice == 5:
                    print("게임을 종료합니다.")
                    break
                actions[choice]()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")
            self.save_state()
