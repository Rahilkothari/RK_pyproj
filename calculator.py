import _tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)

def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)

def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)

def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)

def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)

def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)

def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)

def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)

def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn10_clicked():
    global val
    val = val + "0"
    data.set(val)

def plus():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def minus():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def multiply():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def divide():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def C_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","Division by 0 not supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A/x)
            data.set(C)
            val = str(C)




root = Tk()
root.geometry()
root.resizable()
root.title("Calci")

data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = "se",
    font = ("Verdana",20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000"
)
lbl.pack(expand = True, fill = "both")

btnrow1 = Frame(root,bg="#000000")
btnrow1.pack(expand= True, fill = "both",)

btnrow2 = Frame(root)
btnrow2.pack(expand= True, fill = "both",)

btnrow3 = Frame(root)
btnrow3.pack(expand= True, fill = "both",)

btnrow4 = Frame(root)
btnrow4.pack(expand= True, fill = "both",)

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0,
    command = btn1_clicked,
)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn2_clicked,
)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn3_clicked,
)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = plus,

)
btn4.pack(side= LEFT, expand = True, fill = "both")





btn1 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn4_clicked,
)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn5_clicked,
)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn6_clicked,
)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4 = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=minus,
)
btn4.pack(side= LEFT, expand = True, fill = "both")







btn1 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn7_clicked,

)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn8_clicked,
)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn9_clicked,
)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4 = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=multiply,
)
btn4.pack(side= LEFT, expand = True, fill = "both")






btn1 = Button(
    btnrow4,
    text = "C",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = C_pressed,
)
btn1.pack(side= LEFT, expand = True, fill = "both")

btn2 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn10_clicked,
)
btn2.pack(side= LEFT, expand = True, fill = "both")

btn3 = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = result,
)
btn3.pack(side= LEFT, expand = True, fill = "both")

btn4 = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=divide,
)
btn4.pack(side= LEFT, expand = True, fill = "both")





root.mainloop()

