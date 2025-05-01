class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.answer_count=0
        self.n=len(self.question_list)

    def still_has_question(self):
        return not(self.n==self.question_number)
    

    def check_answer(self,user_answer,current_question):
        if user_answer.lower()==current_question.lower():
            self.answer_count+=1
            print("You got it right!")
        else: 
            print("Wrong!")
            print(f"The correct answer was: {current_question.upper()}")
        print(f"Your current score is: {self.answer_count}/{self.question_number}\n")


    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"\nQ.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)
        
