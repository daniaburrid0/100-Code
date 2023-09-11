import tkinter as tk
from tkinter import PhotoImage
import datetime

class PomodoroTimer:
    WORK_TIME = 25*60
    SHORT_BREAK_TIME = 5*60
    LONG_BREAK_TIME = 20*60
    WORK_COLOR = "#9bdeac"
    SHORT_BREAK_COLOR = "#e7305b"
    LONG_BREAK_COLOR = "#e2979c"
    BACKGROUND_COLOR = "#f7f5dd"

    def __init__(self):
        self.REPS = 0
        self.TIMER = None
        
        self.window = tk.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=self.BACKGROUND_COLOR)
        self.setup_ui()
        self.window.mainloop()

    def setup_ui(self):
        self.timer_label = tk.Label(text="Timer", fg=self.WORK_COLOR, bg=self.BACKGROUND_COLOR,
                            font=("Courier", 50, "bold"))
        self.timer_label.grid(column=1, row=0)

        self.canvas = tk.Canvas(width=203, height=224, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.pomodoro_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(103, 112, image=self.pomodoro_img)
        self.timer_text = self.canvas.create_text(
            103, 130, text="00:00", fill="white", font=("Courier", 35, "bold")
        )
        self.canvas.grid(column=1, row=1)

        self.start_button = tk.Button(text="Start", command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = tk.Button(text="Reset", command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.checkmark = tk.Label(fg=self.WORK_COLOR, bg=self.BACKGROUND_COLOR)
        self.checkmark.grid(column=1, row=3)

    def reset_timer(self):
        self.window.after_cancel(self.TIMER)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.timer_label.config(text="Timer")
        self.checkmark.config(text="")
        self.REPS = 0

    def start_timer(self):
        self.REPS += 1
        self.set_timer()

    def set_timer(self):
        if self.REPS % 8 == 0:
            self.count_down(self.LONG_BREAK_TIME, self.LONG_BREAK_COLOR, "Long Break")
        elif self.REPS % 2 == 0:
            self.count_down(self.SHORT_BREAK_TIME, self.SHORT_BREAK_COLOR, "Short Break")
        else:
            self.count_down(self.WORK_TIME, self.WORK_COLOR, "Work")

    def count_down(self, count, color, mode):
        self.timer_label.config(text=mode, fg=color)
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=count)

        def update_timer():
            time_left = end_time - datetime.datetime.now()
            minutes, seconds = divmod(time_left.seconds, 60)
            self.canvas.itemconfig(self.timer_text, text=f"{minutes:02d}:{seconds:02d}")
            if time_left > datetime.timedelta(seconds=0):
                self.TIMER = self.window.after(1000, update_timer)
            else:
                self.update_checkmark()
                self.start_next_timer()

        update_timer()

    def update_checkmark(self):
        if self.REPS % 2 == 0:
            self.checkmark.config(text="✔" * (self.REPS // 2))

    def start_next_timer(self):
        self.set_timer()

if __name__ == "__main__":
    PomodoroTimer()