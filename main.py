# Emanuel Biruk Seifegebreal --> 2024 - A project for learning purposes

from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
# Create Flash Cards

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(vocab, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


# UI

def flip_card():
    global current_card
    # Flipped Card
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(vocab, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_back_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# Text
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
vocab = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, command=next_card)
wrong_btn.grid(column=0, row=1)

right_btn_image = PhotoImage(file="images/right.png")
right_btn = Button(image=right_btn_image, highlightthickness=0, command=is_known)
right_btn.grid(column=1, row=1)

next_card()

window.mainloop()
