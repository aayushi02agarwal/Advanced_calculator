from tkinter import *
import parser
import math
from math import factorial


root = Tk()
root.title('Advanced-Calculator')

i = 0

def get_variables(num):
    global i
    display.insert(i,num)
    i+=1
 
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
 
# Function which takes operator as input and displays it on the input field
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i,operator)
    i+=length
 
#Function to clear the input field 
def clear_all():
    display.delete(0,END)
 
#Function which works like backspace
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#Function to calculate the factorial and display it

def fact():
            global i
            entire_string = display.get() 
            s='[(+-/*%]'
            c=0
            for i in range(len(entire_string)):
                if entire_string[i] in s:
                    c=i
            e_s = entire_string[c+1:]
        
            if c==0:
                current = factorial(int(entire_string))
                clear_all()
                display.insert(0,current)
            else:
                current = factorial(int(e_s))
                str1 = entire_string[:c]
                clear_all()
                display.insert(0,int(str1)+current)
            length=len(str(current))
            i+=length
        
def tan():
        global i
        entire_string = display.get()
        s='[(+-/*%]'
        c=0
        for i in range(len(entire_string)):
            if entire_string[i] in s:
                c=i
        e_s=entire_string[c+1:]
        if c==0:
            current = math.tan(math.radians(int(entire_string)))
            clear_all()
            display.insert(0,current)
        else:
            current = math.tan(math.radians(int(e_s)))
            display.insert(c+1,current)
        length=len(str(current))
        i+=length



def sin():
        global i
        entire_string = display.get()
        s='[(+-/*%]'
        c=0
        for i in range(len(entire_string)):
            if entire_string[i] in s:
                c=i
        e_s=entire_string[c+1:]
        if c==0:
            current = math.sin(math.radians(int(entire_string)))
            clear_all()
            display.insert(0,current)
        else:
            current = math.sin(math.radians(int(e_s)))
            display.insert(c+1,current)
        length=len(str(current))
        i+=length
        
def cos():
        global i
        entire_string = display.get()
        s='[(+-/*%]'
        c=0
        for i in range(len(entire_string)):
            if entire_string[i] in s:
                c=i
        e_s=entire_string[c+1:]
        if c==0:
            current = math.cos(math.radians(int(entire_string)))
            clear_all()
            display.insert(0,current)
        else:
            current = math.cos(math.radians(int(e_s)))
            display.insert(c+1,current)
        length=len(str(current))
        i+=length

def sqroot():
            global i
            entire_string = display.get() 
            s='[(+-/*%]'
            c=0
            for i in range(len(entire_string)):
                if entire_string[i] in s:
                    c=i
            e_s = entire_string[c+1:]
        
            if c==0:
                current = math.sqrt(int(entire_string))
                clear_all()
                display.insert(0,current)
            else:
                current = math.sqrt(int(e_s))
                str1 = entire_string[:c]
                clear_all()
                display.insert(0,float(str1)+float(current))
            length=len(str(current))
            i+=length
        
display = Entry(root)
display.grid(row=1,columnspan=6,sticky=N+E+W+S)

Button(root,text="1",command = lambda :get_variables(1)).grid(row=2,column=0, sticky=N+S+E+W)
Button(root,text=" 2",command = lambda :get_variables(2)).grid(row=2,column=1, sticky=N+S+E+W)
Button(root,text=" 3",command = lambda :get_variables(3)).grid(row=2,column=2, sticky=N+S+E+W)
 
Button(root,text="4",command = lambda :get_variables(4)).grid(row=3,column=0, sticky=N+S+E+W)
Button(root,text=" 5",command = lambda :get_variables(5)).grid(row=3,column=1, sticky=N+S+E+W)
Button(root,text=" 6",command = lambda :get_variables(6)).grid(row=3,column=2, sticky=N+S+E+W)
 
Button(root,text="7",command = lambda :get_variables(7)).grid(row=4,column=0, sticky=N+S+E+W)
Button(root,text=" 8",command = lambda :get_variables(8)).grid(row=4,column=1, sticky=N+S+E+W)
Button(root,text=" 9",command = lambda :get_variables(9)).grid(row=4,column=2, sticky=N+S+E+W)
 
Button(root,text="AC",command=lambda :clear_all()).grid(row=5,column=0, sticky=N+S+E+W)
Button(root,text=" 0",command = lambda :get_variables(0)).grid(row=5,column=1, sticky=N+S+E+W)
Button(root,text=" .",command=lambda :get_variables(".")).grid(row=5, column=2, sticky=N+S+E+W)
 
 
Button(root,text="+",command= lambda :get_operation("+")).grid(row=2,column=3, sticky=N+S+E+W)
Button(root,text="-",command= lambda :get_operation("-")).grid(row=3,column=3, sticky=N+S+E+W)
Button(root,text="*",command= lambda :get_operation("*")).grid(row=4,column=3, sticky=N+S+E+W)
Button(root,text="/",command= lambda :get_operation("/")).grid(row=5,column=3, sticky=N+S+E+W)
 
Button(root,text="pi",command= lambda :get_operation("*3.14")).grid(row=2,column=4, sticky=N+S+E+W)
Button(root,text="%",command= lambda :get_operation("%")).grid(row=3,column=4, sticky=N+S+E+W)
Button(root,text="(",command= lambda :get_operation("(")).grid(row=4,column=4, sticky=N+S+E+W)
Button(root,text="exp",command= lambda :get_operation("**")).grid(row=5,column=4, sticky=N+S+E+W)
 
Button(root,text="tan",command= lambda :tan()).grid(row=2,column=5, sticky=N+S+E+W)
Button(root,text="cos", command= lambda: cos()).grid(row=3,column=5, sticky=N+S+E+W)
Button(root,text="sin",command= lambda : sin()).grid(row=4,column=5, sticky=N+S+E+W)
Button(root,text="sqrt",command= lambda : sqroot()).grid(row=5,column=5, sticky=N+S+E+W)

Button(root,text="<-",command= lambda :undo()).grid(row=2,column=6, sticky=N+S+E+W)
Button(root,text="x!", command= lambda: fact()).grid(row=3,column=6, sticky=N+S+E+W)
Button(root,text=")",command= lambda :get_operation(")")).grid(row=4,column=6, sticky=N+S+E+W)
Button(root,text="^2",command= lambda :get_operation("**2")).grid(row=5,column=6, sticky=N+S+E+W)


Button(root,text="=",command= lambda :calculate()).grid(columnspan=6, sticky=N+S+E+W)

 
root.mainloop()
