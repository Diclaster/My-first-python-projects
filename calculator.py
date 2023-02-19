from tkinter import *

root = Tk()
root["bg"] = "black"
root.geometry("485x550+200+200")
root.title("Calc")
root.resizable(False, False)
lbl = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
lbl.place(x=11, y=50)
btns = ['.', 'C', 'DEL', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', '7', '8', '9', '-', '(', '0', ')', 'x^2']


def set_value(formula):
    lbl['text'] = str(eval(formula))


def logicalc(operator):
    if operator == "C":
        lbl['text']='0'
    elif operator == "DEL":
        lbl['text']=lbl['text'][0:-1]
    elif operator == 'x^2':
        lbl['text']=str(eval(int(lbl['text']))**2)
    elif operator == "=":
        set_value(lbl['text'])
    else:
        if lbl['text'] == "0":
            lbl['text'] = ""
        lbl['text'] = lbl['text'] + operator


x = 361
y = 60
for bt in btns:
    com = lambda x=bt: logicalc(x)
    Button(text=bt, bg='white', font=('consolas', 15), command=com).place(x=x, y=y, width=115, heigh=79)
    x += 117
    if x > 400:
        x = 10
        y += 81
root.mainloop()

