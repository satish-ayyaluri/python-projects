BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas


to_learn=[]
try:
    word=pandas.read_csv("data/Words_To_Learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=word.to_dict(orient="records")
def generate_button():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)

    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(card_background,image=front_image)
    canvas.itemconfig(word_text,text=current_card["French"],fill="black")
    flip_timer=window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/Words_To_Learn.csv",index=False)
    generate_button()



current_card=random.choice(to_learn)
french_card=current_card["French"]
english_card=current_card["English"]

def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=back_image)

window=Tk()
window.title("card flip")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)



back_image=PhotoImage(file="images/card_back.png")
front_image=PhotoImage(file="images/card_front.png")
right_image=PhotoImage(file="images/right.png")
wrong_png=PhotoImage(file="images/wrong.png")

canvas=Canvas(width=800,height=526,highlightthickness=0)

card_background=canvas.create_image(400,263,image=front_image)
title=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word_text=canvas.create_text(400,263,text=f"{french_card}",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

flip_timer=window.after(3000, func=flip_card)


unknown_button=Button(image=wrong_png,highlightthickness=0,command=generate_button)
unknown_button.grid(row=1,column=0)

check_button=Button(image=right_image,highlightthickness=0,command=is_known)
check_button.grid(row=1,column=1)


window.mainloop()
