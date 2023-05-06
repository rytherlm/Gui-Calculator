'''
Aidan Ryther
Caculator 
November 25,2022
'''


from tkinter import *
root = Tk() #my personal calculator using tinker adn python 
root.title("Calculator")


enter = Entry(root,width=35, borderwidth=5)
enter.grid(row=0,column=0,columnspan=3,padx=10,pady=10)



def click_click(number):
    current = enter.get()
    enter.delete(0, END)
    enter.insert(0,str(current) + str(number))

def click_clear():
    enter.delete(0, END)

def click_equal():
    second_number = enter.get()
    enter.delete(0,END)

    if var == 'addition':
        enter.insert(0, x + int(second_number))
    if var == 'subtraction':
        enter.insert(0, x - int(second_number))
    if var == 'multiply':
        enter.insert(0, x * int(second_number))
    if var == 'divide':
        enter.insert(0, x / int(second_number))


#the var more the results
def click_add():
    first_number = enter.get()
    global x
    global var
    var = 'addition'
    x = float(first_number)
    enter.delete(0, END)

def click_subtract():
    first_number = enter.get()
    global x
    global var
    var = 'subtraction'
    x = float(first_number)
    enter.delete(0, END)

def click_multiply():
    first_number = enter.get()
    global x
    global var
    var = 'multiply'
    x = float(first_number)
    enter.delete(0, END)

def click_divide():
    first_number = enter.get()
    global x
    global var
    var = 'divide'
    x = float(first_number)
    enter.delete(0, END)
def helper_log(base,n):
    count = 0
    
    while (n < 1):
        n = n/b
        

#n is the number being found by the logarthim and the base is what is being mutlipled 
# def clcik_logarthim():
    
    


#the buttons are able to be pressed now
click_1 = Button(root,text = '1',padx=40,pady=20,command=lambda: click_click(1),fg='slategrey')
click_2 = Button(root,text = '2',padx=40,pady=20,command=lambda: click_click(2),fg='slategrey')
click_3 = Button(root,text = '3',padx=40,pady=20,command=lambda: click_click(3),fg='slategrey')

click_4 = Button(root,text = '4',padx=40,pady=20,command=lambda: click_click(4),fg='slategrey')
click_5 = Button(root,text = '5',padx=40,pady=20,command=lambda: click_click(5),fg='slategrey')
click_6 = Button(root,text = '6',padx=40,pady=20,command=lambda: click_click(6),fg='slategrey')

click_7 = Button(root,text = '7',padx=40,pady=20,command=lambda: click_click(7),fg='slategrey')
click_8 = Button(root,text = '8',padx=40,pady=20,command=lambda: click_click(8),fg='slategrey')
click_9 = Button(root,text = '9',padx=40,pady=20,command=lambda: click_click(9),fg='slategrey')
click_0 = Button(root,text = '0',padx=40,pady=20,command=lambda: click_click(0),fg='slategrey')

click_add1 = Button(root,text = '+',padx=40,pady=20,command=click_add,fg='slategrey')
click_equal1 = Button(root,text = '=',padx=40,pady=20,command=click_equal,fg='slategrey')
click_clear1 = Button(root,text = 'clear',padx=150,pady=20,command=click_clear,fg='slategrey')

click_subtract1 = Button(root,text = '-',padx=40,pady=20,command=click_subtract,fg='slategrey')
click_multiply1 = Button(root,text = 'x',padx=40,pady=20,command=click_multiply,fg='slategrey')
click_divide1 = Button(root,text = '/',padx=40,pady=20,command=click_divide,fg='slategrey')



#the 1/2/3 button
click_1.grid(row=1,column=0)
click_2.grid(row=1,column=1)
click_3.grid(row=1,column=2)

#the 4/5/6 button
click_4.grid(row=2,column=0)
click_5.grid(row=2,column=1)
click_6.grid(row=2,column=2)

# the 7/8/9 button
click_7.grid(row=3,column=0)
click_8.grid(row=3,column=1)
click_9.grid(row=3,column=2)

#the add.subtract/zero burron
click_add1.grid(row=4,column=1)
click_subtract1.grid(row=4,column=2)
click_0.grid(row=4,column=0)

#the multiply/divide/equals button
click_multiply1.grid(row=5,column=0)
click_divide1.grid(row=5,column=1)
click_equal1.grid(row=5,column=2)


#the clear button
click_clear1.grid(row=6,column=0,columnspan=3)


root.mainloop()