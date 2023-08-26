class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer)
    
    def check_answer(self, user_answer):
        if user_answer.lower() == self.question_list[self.question_number - 1].answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print("Your current score is: " + str(self.score)+"/"+str(len(self.question_list)))
        print("\n")