from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    new_question = Question(items["question"], items["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")