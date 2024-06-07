from tkinter import *
import random
import linecache

screen = Tk()

screen.geometry("600x500")
screen.title("Typing speed")

score = 0
State = NORMAL
timeLeft = 60

def nexttext():
    global score
    global timeLeft

    if timeLeft > 0:

        randomness = random.randint(1, 400000)
        print(randomness)
        info = linecache.getline(r"words.txt", randomness)

        info = info.strip()

        print(info)
        if Entry1.get().lower() == info:
            score += len(info)
        Entry1.delete(0, END)

        label.configure(text=info)
        ScoreLabel.configure(text="Score: " + str(score))




def countdown():
    global timeLeft
    global State

    if timeLeft == 0:
        State = DISABLED
        Entry1.configure(state=State)
        label.configure(text="CPS: " + str((score/60)))
    if timeLeft > 0:
        timeLeft -= 1
        TimeLeftLabel.configure(text="Time: " + str(timeLeft))
        TimeLeftLabel.after(1000, countdown)


def start(event):
    if timeLeft == 60:
        countdown()
    if timeLeft <= 59:
        ScoreLabel.configure(text="Score: " + str(score))
    nexttext()


WelcomeLabel = Label(screen, text="Type in the text that is displayed on your screen!", fg="black", font=("Bold", 15))
WelcomeLabel.pack()

TimeLeftLabel = Label(screen, text="Time left: " + str(timeLeft), fg="black", font=("Bold", 15))
TimeLeftLabel.pack()

ScoreLabel = Label(screen, text="Score: " + str(score), fg="black", font=("Bold", 15))
ScoreLabel.pack()

label = Label(screen, text="", fg="black", font=("Bold", 25))
label.pack()

Entry1 = Entry(screen, width=20, state=State)
Entry1.pack()

screen.bind("<Return>", start)

screen.mainloop()
