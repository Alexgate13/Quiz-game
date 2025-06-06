from tkinter import *
from tkinter.ttk import *


screen = Tk()
screen.geometry('300x300')
screen.title('My first window')
#screen.configure(background="black")

score = 0
timer = 10

def start():
    q0()
    if timer == 10:
        countdown()

def countdown():
    global timer
    if timer > 0:
        timer -= 1
        lbl2.configure(text="Time:" + str(timer))
        lbl2.after(1000, countdown)

def nextQestion():
    global score
    if timer > 0:
        if choice.get() == a1():
            score += 1
        lbl1.configure(text="Score:" + str(score))
    print(score)


lbl1 = Label(screen, text="score:0")
lbl1.pack()

lbl2 = Label(screen, text="Time left:10")
lbl2.pack()

def clear():
    for widget in screen.winfo_children():
        widget.destroy()

def a0():
    clear()
    q1()

def a1():
    global choice
    a = choice.get()
    if a == 3:
        print("Correct")
    else:
        print("Wrong")

    clear()
    q2()

def a2():
    global choice
    a = choice.get()
    if a == 2:
        print("Correct")
    else:
        print("Wrong")

    clear()
    q3()

def a3():
    global choice
    a = choice.get()
    if a == 1:
        print("Correct")
    else:
        print("Wrong")

    clear()
    q4()

def a4():
    global choice
    a = choice.get()
    if a == 1:
        print("Correct")
    else:
        print("Wrong")
    clear()
    q5()

def a5():
    global choice
    a = choice.get()
    if a == 3:
        print("Correct")
    else:
        print("Wrong")


def q0():

    Btn0 = Button(screen, text="Start", command=a0)
    Btn0.pack()



def q1():
    global choice

    choice = IntVar()
    rb0 = Label(screen, text="1. What is the capital of Japan?")#, background="black", foreground="white"
    rb1 = Radiobutton(screen, text="A. Beijing", value=1, variable=choice)
    rb2 = Radiobutton(screen, text="B. Seoul", value=2, variable=choice)
    rb3 = Radiobutton(screen, text="C. Tokyo", value=3, variable=choice)


    rb0.pack()
    rb1.pack()
    rb2.pack()
    rb3.pack()


    Btn1 = Button(screen, text="Next", command=a1)
    Btn1.pack()



def q2():
    global choice



    choice = IntVar()
    rb4 = Label(screen, text="2. Which planet is known as the Red Planet?")
    rb5 = Radiobutton(screen, text="A. Venus", value=1, variable=choice)
    rb6 = Radiobutton(screen, text="B. Mars", value=2, variable=choice)
    rb7 = Radiobutton(screen, text="C. Jupiter", value=3, variable=choice)


    rb4.pack()
    rb5.pack()
    rb6.pack()
    rb7.pack()


    Btn2 = Button(screen, text="Next", command=a2)
    Btn2.pack()



def q3():
    global choice



    choice = IntVar()
    rb8 = Label(screen, text="3. What is the chemical symbol for water?")
    rb9 = Radiobutton(screen, text="A. H2O", value=1, variable=choice)
    rb10 = Radiobutton(screen, text="B. O2", value=2, variable=choice)
    rb11 = Radiobutton(screen, text="C. CO2", value=3, variable=choice)


    rb8.pack()
    rb9.pack()
    rb10.pack()
    rb11.pack()


    Btn3 = Button(screen, text="Next", command=a3)
    Btn3.pack()



def q4():
    global choice



    choice = IntVar()
    rb12 = Label(screen, text="4. Who wrote the play 'Romeo and Juliet'?")
    rb13 = Radiobutton(screen, text="A. William Shakespeare", value=1, variable=choice)
    rb14 = Radiobutton(screen, text="B. Charles Dickens", value=2, variable=choice)
    rb15 = Radiobutton(screen, text="C. Mark Twain", value=3, variable=choice)


    rb12.pack()
    rb13.pack()
    rb14.pack()
    rb15.pack()


    Btn4 = Button(screen, text="Next", command=a4)
    Btn4.pack()



def q5():
    global choice



    choice = IntVar()
    rb16 = Label(screen, text="5. Which country is famous for the Eiffel Tower?")
    rb17 = Radiobutton(screen, text="A. Italy", value=1, variable=choice)
    rb18 = Radiobutton(screen, text="B. Spain", value=2, variable=choice)
    rb19 = Radiobutton(screen, text="C. France", value=3, variable=choice)


    rb16.pack()
    rb17.pack()
    rb18.pack()
    rb19.pack()


    Btn5 = Button(screen, text="Next", command=a5)
    Btn5.pack()









q0()




screen.mainloop()