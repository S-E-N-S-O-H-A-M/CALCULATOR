from tkinter import *

calci=Tk()
calci.title('CALCULATOR')
calci.iconbitmap('CALCI.ico')
calci.geometry("185x185")

expression = ""

def input_number(number, equation):
   global expression
   expression = expression + str(number)
   equation.set(expression)
def clear_input_field(equation):
   global expression
   expression = ""
   equation.set('0')
def evaluate(equation):
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        expression = ""
def my_calci():
    equation = StringVar()
    equation.set('0')
    display=Entry(calci,textvariable=equation,bg='white',fg="black",font="Lato 12 bold",borderwidth=2,relief="groove")
    display.grid(columnspan=4)
    seven=Button(calci,text='7', command=lambda: input_number(7, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    seven.grid(row=1,column=0,sticky=N+S+E+W)
    eight=Button(calci,text='8', command=lambda: input_number(8, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    eight.grid(row=1,column=1,sticky=N+S+E+W)
    nine=Button(calci,text='9', command=lambda: input_number(9, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    nine.grid(row=1,column=2,sticky=N+S+E+W)
    ce=Button(calci,text='C', command=lambda:  clear_input_field(equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    ce.grid(row=1,column=3,sticky=N+S+E+W)
    four=Button(calci,text='4', command=lambda: input_number(4, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    four.grid(row=2,column=0,sticky=N+S+E+W)
    five=Button(calci,text='5', command=lambda: input_number(5, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    five.grid(row=2,column=1,sticky=N+S+E+W)
    six=Button(calci,text='6', command=lambda: input_number(6, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    six.grid(row=2,column=2,sticky=N+S+E+W)
    multiplication=Button(calci,text='*', command=lambda: input_number('*', equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    multiplication.grid(row=2,column=3,sticky=N+S+E+W)
    one=Button(calci,text='1', command=lambda: input_number(1, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    one.grid(row=3,column=0,sticky=N+S+E+W)
    two=Button(calci,text='2', command=lambda: input_number(2, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    two.grid(row=3,column=1,sticky=N+S+E+W)
    three=Button(calci,text='3', command=lambda: input_number(3, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    three.grid(row=3,column=2,sticky=N+S+E+W)
    divide=Button(calci,text='/', command=lambda: input_number('/', equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    divide.grid(row=3,column=3,sticky=N+S+E+W)
    plus=Button(calci,text='+', command=lambda: input_number('+', equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    plus.grid(row=4,column=0,sticky=N+S+E+W)
    zero=Button(calci,text='0', command=lambda: input_number(0, equation),bg='white',fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    zero.grid(row=4,column=1,sticky=N+S+E+W)
    minus=Button(calci,text='-', command=lambda: input_number('-', equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    minus.grid(row=4,column=2,sticky=N+S+E+W)
    equal=Button(calci,text='=', command=lambda:  evaluate(equation),bg="#F3F4F6",fg="black",font="Lato 12 bold",padx="5",pady="5",borderwidth=2,relief="groove")
    equal.grid(row=4,column=3,sticky=N+S+E+W)

my_calci()       
calci.mainloop()
