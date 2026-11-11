class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices        
        self.answer = answer


    def show(self):
        print(self.question)
        for i,j in enumerate(self.choices,1):
            print(f'{i}.{j}')

    def is_correct(self,user_answer):
        self.answer == user_answer # 비교 연산자 자체 결과 타입 bool
