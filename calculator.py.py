import tkinter as tk
import math

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("420x600")
root.configure(bg="#1e1e2f")

expression = ""
equation = tk.StringVar()

display = tk.Entry(root, textvariable=equation,
                   font=("Arial", 28),
                   bd=0,
                   bg="#2d2d44",
                   fg="white",
                   justify="right")
display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, padx=10, pady=20)



def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def square():
    global expression
    try:
        value = float(expression)
        result = value ** 2
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        value = float(expression)
        result = math.sqrt(value)
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

def percent():
    global expression
    try:
        value = float(expression)
        result = value / 100
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""
        

btn_style = {
    "font": ("Arial", 16),
    "bd": 0,
    "width": 5,
    "height": 2,
    "fg": "white"
}


buttons = [
    ('C',1,0,"#ff5c5c",clear),
    ('DEL',1,1,"#ff5c5c",delete),
    ('%',1,2,"#4cc9f0",percent),
    ('/',1,3,"#f72585",lambda: press('/')),

    ('7',2,0,"#3a3a5c",lambda: press('7')),
    ('8',2,1,"#3a3a5c",lambda: press('8')),
    ('9',2,2,"#3a3a5c",lambda: press('9')),
    ('*',2,3,"#f72585",lambda: press('*')),

    ('4',3,0,"#3a3a5c",lambda: press('4')),
    ('5',3,1,"#3a3a5c",lambda: press('5')),
    ('6',3,2,"#3a3a5c",lambda: press('6')),
    ('-',3,3,"#f72585",lambda: press('-')),

    ('1',4,0,"#3a3a5c",lambda: press('1')),
    ('2',4,1,"#3a3a5c",lambda: press('2')),
    ('3',4,2,"#3a3a5c",lambda: press('3')),
    ('+',4,3,"#f72585",lambda: press('+')),

    ('x²',5,0,"#4cc9f0",square),
    ('√',5,1,"#4cc9f0",sqrt),
    ('0',5,2,"#3a3a5c",lambda: press('0')),
    ('=',5,3,"#7209b7",equal),
]

for (text,row,col,color,command) in buttons:
    tk.Button(root,
              text=text,
              bg=color,
              command=command,
              **btn_style).grid(row=row, column=col, padx=8, pady=8)

root.mainloop()
