from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def question_bank_maker():
    question_bank = []

    for question in question_data:
        question_text = question["text"]
        question_answer = question["answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return question_bank

def main():
    question_bank = question_bank_maker()
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
    
if __name__ == "__main__":
    main()        