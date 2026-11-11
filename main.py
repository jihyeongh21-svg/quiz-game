def menu():
    print("========================================")
    print("🎯 나만의 퀴즈 게임 🎯")
    print("1. 퀴즈풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수확인")
    print("5. 종료")
    print("========================================")
    choice = input("메뉴 선택: ")
    return choice


def main():
    while True:
        choice = menu()
        if choice == '1':
            print("퀴즈시작")
        elif choice == '2':
            print("퀴즈추가")
        elif choice == '3':
            print("퀴즈목록")
        elif choice == "4":
            print("점수확인")
        elif choice == '5':
            print("플레이 해주셔서 감사합니다")
            break
        else:
            print("잘못된 입력입니다 다시 입력 해주세요")

if __name__ == "__main__":
    main()
