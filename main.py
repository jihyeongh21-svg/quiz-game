"""터미널 퀴즈 게임."""


class Quiz:
    """객관식 퀴즈 한 문제."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices  # 선택지 4개
        self.answer = answer    # 정답 번호 (1~4)

    def display(self, number=None):
        title = f"[문제 {number}] " if number else ""
        print(f"\n{title}{self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


def create_default_quizzes():
    """주제: 파이썬 기초 문법 퀴즈 6개."""
    return [
        Quiz("Python의 창시자는?", ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"], 1),
        Quiz("리스트를 나타내는 기호는?", ["()", "[]", "{}", "<>"], 2),
        Quiz("정수 자료형의 이름은?", ["str", "bool", "int", "dict"], 3),
        Quiz("반복 횟수가 정해진 반복에 주로 쓰는 문법은?", ["if", "for", "def", "try"], 2),
        Quiz("함수를 정의할 때 쓰는 키워드는?", ["func", "lambda", "define", "def"], 4),
        Quiz("키-값 쌍으로 데이터를 저장하는 자료형은?", ["dict", "list", "tuple", "set"], 1),
    ]


def read_int(prompt, low, high):
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


def show_menu():
    print("\n===== 파이썬 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def play_quiz(quizzes):
    """모든 퀴즈를 순서대로 출제하고 맞힌 개수를 반환한다. 퀴즈가 없으면 None."""
    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return None
    score = 0
    for number, quiz in enumerate(quizzes, start=1):
        quiz.display(number)
        user_answer = read_int("정답 번호(1~4): ", 1, 4)
        if quiz.is_correct(user_answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")
    print(f"\n결과: {len(quizzes)}문제 중 {score}문제 정답")
    return score


def read_text(prompt):
    """빈 문자열이 아닌 텍스트를 입력받는다."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("입력이 비어 있습니다. 다시 입력해 주세요.")


def add_quiz(quizzes):
    """사용자에게 문제·선택지 4개·정답 번호를 입력받아 추가한다."""
    question = read_text("문제: ")
    choices = [read_text(f"선택지 {i}: ") for i in range(1, 5)]
    answer = read_int("정답 번호(1~4): ", 1, 4)
    quizzes.append(Quiz(question, choices, answer))
    print("퀴즈가 추가되었습니다.")


def main():
    quizzes = create_default_quizzes()
    while True:
        show_menu()
        choice = read_int("선택: ", 1, 5)
        if choice == 1:
            play_quiz(quizzes)
        elif choice == 2:
            add_quiz(quizzes)
        elif choice == 5:
            print("게임을 종료합니다.")
            break
        else:
            print("(준비 중인 기능입니다)")


if __name__ == "__main__":
    main()
