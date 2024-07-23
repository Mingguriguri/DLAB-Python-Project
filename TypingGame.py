'''
Tkinter를 이용한 간단한 타이핑 게임
'''
from tkinter import *
import random

def start_game(event=None):
    global score, missed, time_left
    if time_left == 60:
        countdown()
    if entry.get() == word_label.cget("text"):
        score += 1
    else:
        missed += 1
    score_label.config(text="점수: " + str(score))
    missed_label.config(text="틀린 수: " + str(missed))
    new_word()

def new_word():
    words = ['python', 'javascript', 'java', 'html', 'css', 'tkinter', 'algorithm', 'development', 'framework', 'backend', 'frontend']
    random_word = random.choice(words)
    word_label.config(text=random_word)
    entry.delete(0, END)

def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_label.config(text="남은 시간: " + str(time_left))
        root.after(1000, countdown)
    else:
        word_label.config(text="게임 종료!")
        entry.config(state='disabled')

def start_timer():
    global score, missed, time_left
    score = 0
    missed = 0
    time_left = 60
    score_label.config(text="점수: 0")
    missed_label.config(text="틀린 수: 0")
    time_label.config(text="남은 시간: 60")
    word_label.config(text="")
    entry.config(state='normal')
    new_word()
    entry.focus()
    countdown()

root = Tk()
root.title("타이핑 게임")

score = 0
missed = 0
time_left = 60

frame = Frame(root)
frame.pack()

word_label = Label(frame, text="", font=("Arial", 24))
word_label.pack()

entry = Entry(frame, font=("Arial", 24))
entry.pack()
entry.bind("<Return>", start_game)

start_button = Button(root, text="게임 시작", font=("Arial", 18), command=start_timer)
start_button.pack()

score_label = Label(root, text="점수: 0", font=("Arial", 18))
score_label.pack()

missed_label = Label(root, text="틀린 수: 0", font=("Arial", 18))
missed_label.pack()

time_label = Label(root, text="남은 시간: 60", font=("Arial", 18))
time_label.pack()

root.mainloop()
