"""터미널 퀴즈 게임."""


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
