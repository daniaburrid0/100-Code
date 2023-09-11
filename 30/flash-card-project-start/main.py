from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_LANG = ("Arial", 20, "italic")
FONT_WORD = ("Arial", 40, "bold")

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    words_to_learn = data.to_dict(orient="records")

def flip_card():
    global word
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=word["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)

def random_word():
    global words_to_learn, word, flip_timer
    windows.after_cancel(flip_timer)
    canvas.itemconfig(canvas_img, image=card_front_img)
    word = random.choice(words_to_learn)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=word["French"], fill="black")
    flip_timer = windows.after(3000, func=flip_card)
    print(len(words_to_learn))
    check_button.config(command=remove_word)

def remove_word():
    global words_to_learn
    words_to_learn.remove(word)
    data = pd.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_word()

# Window
windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Timer flip
flip_timer = windows.after(3000, func=flip_card)
# Canvas card front
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

# Camvas card back
card_back_img = PhotoImage(file="images/card_back.png")

# Canvas label language
language_label = canvas.create_text(400, 150, text="", font=FONT_LANG)

# Canvas label word
word_label = canvas.create_text(400, 263, text="", font=FONT_WORD)

# X button
x_button_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_button_img, highlightthickness=0, command=random_word)
x_button.grid(row=1, column=0)

# Check button
check_button_img = PhotoImage(file="images/right.png")
check_button = Button(image=check_button_img, highlightthickness=0, command=random_word)
check_button.grid(row=1, column=1)

random_word()
windows.mainloop()