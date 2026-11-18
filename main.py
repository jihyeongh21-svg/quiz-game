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


def main():
    while True:
        show_menu()
        choice = read_int("선택: ", 1, 5)
        if choice == 5:
            print("게임을 종료합니다.")
            break
        print("(준비 중인 기능입니다)")


if __name__ == "__main__":
    main()
