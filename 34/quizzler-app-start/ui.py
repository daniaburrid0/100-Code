from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.set_up_ui()
        self.get_next_question()
        self.window.mainloop()

    def set_up_ui(self):
        # make the score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # make the canvas white
        self.canvas = Canvas(width=290, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # make the question text
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Question text", fill=THEME_COLOR, font=FONT)

        # make the true button
        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        # make the false button4
        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_answer(self):
        response = self.quiz.check_answer("True")
        self.give_feedback(response)
    
    def false_answer(self):
        response = self.quiz.check_answer("False")
        self.give_feedback(response)
        
    def give_feedback(self, response):
        if response == 1:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)