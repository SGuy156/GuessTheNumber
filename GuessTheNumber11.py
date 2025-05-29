from tkinter import *

from tkinter import PhotoImage
import random
import os,sys

def resource_path(relative_path):
    try:
        base_path=sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



screen = Tk() #creates window
screen.title("Guess The Number") # Title
screen.geometry('300x300') #window dimensions - megethos
screen.resizable(height=False, width=False)

tries = 0
highscore = 999999999999

def closing():
    screen.destroy()

def randomize():
    global tries
    tries = 0
    print("randomize")
    lbl.configure(text="Tries:")
    entry.delete(0, END)
    entry.config(state="normal")
    global randNumber
    check = choice.get()


    if check == 1:
        randNumber = random.randint(0, 50)
        print(randNumber)
    elif check == 2:
        randNumber = random.randint(0, 100)
        print(randNumber)
    elif check == 3:
        randNumber = random.randint(0, 200)
        print(randNumber)


def guess(event):
    entryinput = entry.get()
    global tries
    global highscore
    if int(entryinput) == randNumber:
        startlbl.configure(image=check)
        tries = tries + 1
        lbl.configure(text="Tries:" + str(tries))
        entry.delete(0, END)
        entry.config(state="readonly")
        if tries < highscore:
            highscore = tries
            lblhs.config(text="High Score:"+str(highscore))
        tries = 0

    elif int(entryinput) > randNumber:
        startlbl.configure(image=down)
        tries = tries + 1
        entry.delete(0, END)
        lbl.configure(text="Tries:" + str(tries))
    elif int(entryinput) < randNumber:
        startlbl.configure(image=up)
        tries = tries + 1
        entry.delete(0, END)
        lbl.configure(text="Tries:"+str(tries))

tries = 0

lbltitle = Label(screen,text = "Guess The Number!",font=(20))
choice = IntVar()#variable with integers
choice.set(2)
rb1 = Radiobutton(screen,text="Easy: 0-50",value=1,variable=choice)
rb2 = Radiobutton(screen,text="Medium:0-100",value=2,variable=choice)
rb3 = Radiobutton(screen,text="Hard:0-200",value=3, variable =choice)


lbl1 = Label(screen,text = "Try and find the random selected number!")
btne = Button(screen,text="Exit",command=closing)
btnr = Button(screen,text="Begin",command=randomize)

entry = Entry(screen)
entry.config(state="disabled")
lbl = Label(screen,text = "Tries:")
lbldif = Label(screen,text = "Difficulty:")
lblhs = Label(screen,text="High Score:")

start = PhotoImage(file=resource_path("questionmark.png"))
startlbl = Label(screen, image=start)
up = PhotoImage(file=resource_path("arrowup.png"))
uplbl = Label(screen, image=up)
down = PhotoImage(file=resource_path("arrowdown.png"))
downlbl = Label(screen, image=down)
check = PhotoImage(file=resource_path("checkmark.png"))
checklbl = Label(screen, image=check)
check = PhotoImage(file=resource_path("checkmark.png"))
checklbl = Label(screen, image=check)


lbldif.grid(row=0, columnspan=5)
lbl.grid(row=6, columnspan=5)

rb1.grid(row=1,column=1)
rb2.grid(row=1,column=2)
rb3.grid(row=1,column=3)
lbl1.grid(row=2,columnspan=5)
btne.grid(row=3,column=3)
btnr.grid(row=3,column=1)
entry.grid(row=3,column=2)
startlbl.grid(row=5,column=2)
lblhs.grid(row=7, columnspan=5)

screen.bind('<Return>', guess)

screen.mainloop() #teleftaia