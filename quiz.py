"""Quiz 클래스: 객관식 퀴즈 한 문제."""


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

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}

    @classmethod
    def from_dict(cls, data):
        """dict에서 Quiz를 만든다. 형식이 잘못되면 ValueError."""
        question, choices, answer = data["question"], data["choices"], data["answer"]
        valid = (
            isinstance(question, str) and question.strip()
            and isinstance(choices, list) and len(choices) == 4
            and all(isinstance(c, str) for c in choices)
            and isinstance(answer, int) and not isinstance(answer, bool)
            and 1 <= answer <= 4
        )
        if not valid:
            raise ValueError("잘못된 퀴즈 형식")
        return cls(question, choices, answer)
