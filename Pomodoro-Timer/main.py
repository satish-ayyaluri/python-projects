from tkinter import *
import math
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

def reset_timer():
    global reps,timer
    reps = 0
    if timer:
        window.after_cancel(timer)
        timer=None
    canvas.itemconfig(timer_text,text="00:00")
    my_label.config(text="Timer",fg=GREEN)
    check_mark.config(text="")














def start_timer():

    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    if reps%8==0:
        my_label.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 50))
        count_down(long_break)
    elif reps%2==0:
        my_label.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 50))
        count_down(short_break)
    else:

        my_label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
        count_down(work_sec)




def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec:02d}")
    if count>0:
        global timer
        timer= window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            mark+="✓"
        check_mark.config(text=mark)

window=Tk()
window.title("Pomodoro")
window.config(pady=50,padx=103,bg=YELLOW)



my_label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,50))
my_label.grid(column=1,row=0)



canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,111.5,image=tomato_img)
timer_text=canvas.create_text(100,131.5,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=1)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=1)


check_mark=Label(text="",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=2)










window.mainloop()