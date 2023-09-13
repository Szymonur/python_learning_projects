from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_1 = "French"
LANG_2 = "English"

#  ----------------- DATA ------------------
df = pandas.read_csv("./data/french_words.csv")
words = df.to_dict(orient="records")


#  ---------------- LOGIC ------------------

def change_card(word):
    canvas.itemconfig(label_word, text=word)


def new_word(good_answer):
    random_word = random.choice(words)
    canvas.itemconfig(label_word, text=random_word[LANG_1])
    window.after(3000, change_card(random_word[LANG_2]))



#  ------------------ UI ------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front = PhotoImage(file="./images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front)

label_language = canvas.create_text(400, 150, text=LANG_1, font=("Ariel", 40, "italic"), fill="black")
label_word = canvas.create_text(400, 263, text="123", font=("Ariel", 60, "bold"), fill="black")
wrong_image = PhotoImage(file="./images/wrong.png")
btn_wrong = Button(image=wrong_image, highlightthickness=0, command=lambda: new_word(False))
right_image = PhotoImage(file="./images/right.png")
btn_right = Button(image=right_image, highlightthickness=0, command=lambda: new_word(True))

canvas.grid(column=0, row=0, columnspan=2)
btn_wrong.grid(column=0, row=1)
btn_right.grid(column=1, row=1)

mainloop()
