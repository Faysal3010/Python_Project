from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for q in question_data:
    quiz=Question(q['text'],q['answer'])
    question_bank.append(quiz)

question=QuizBrain(question_bank)
    
while question.still_has_question():
    question.next_question()

