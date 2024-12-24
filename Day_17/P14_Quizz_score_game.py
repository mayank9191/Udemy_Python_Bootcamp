from data import question_data
import random

n = 0
score = 0


class Question:
    def __init__(self, ques, ans):
        self.question = ques
        self.answer = ans.lower()


question = []

for i in question_data:
    question_text = i["question"]
    question_answer = i["correct_answer"]
    new_question = Question(question_text, question_answer)
    question.append(new_question)


class QuizBrain:
    def check(self, obj, choice):
        if (obj[n].answer == choice):
            return False

        else:
            return True


brain = QuizBrain()

while (n < len(question)):

    choice = input(f"Q.{n+1} {question[n].question}. (True/False)?: ").lower()

    if (brain.check(question, choice)):
        print(f'''That's wrong.\nThe correct answer was: {
              question[n].answer}.\nYour current score is: {score}/{n+1}''')
    else:
        score += 1
        print(f"You got it right!\nYour current score is: {score}/{n+1}")

    n += 1

print(f"Quiz finished! Your final score is: {score}/{len(question)}")
