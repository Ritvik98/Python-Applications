#A program to build a simple calculator

from tkinter import  *  #importing tkinter libraries


def btnclk(numbers):   #Function to take and store input data in String form
    global opr
    opr=opr+str(numbers)
    text_inp.set(opr)

def btnclr():    #Function to Clear the screen using clear button
    global opr
    opr=""
    text_inp.set("")

def btneq():     #Function to display the value of the given expression
    global opr
    cal=str(eval(opr))
    text_inp.set(cal)
    opr=""

root=Tk()      #Command to generate a window

root.title("Simple Calculator")    #Command to give window a title
opr=""
text_inp=StringVar()

disp=Entry(root, font=("arial",20,"bold"), textvariable=text_inp, bd=30, insertwidth=4, bg="grey", justify="right").grid(columnspan=5)

b7=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="7", bg="grey", command=lambda:btnclk(7)).grid(row=1,column=0)

b8=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="8", bg="grey", command=lambda:btnclk(8)).grid(row=1,column=1)

b9=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="9", bg="grey", command=lambda:btnclk(9)).grid(row=1,column=2)

bC=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="C", bg="grey", command=btnclr).grid(row=1,column=3)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

b4=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="4", bg="grey", command=lambda:btnclk(4)).grid(row=2,column=0)

b5=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="5", bg="grey", command=lambda:btnclk(5)).grid(row=2,column=1)

b6=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="6", bg="grey", command=lambda:btnclk(6)).grid(row=2,column=2)

bp=Button(root, padx=16, pady=16,bd=6, fg="White", font=("arial",20,"bold"), text="*", bg="grey", command=lambda:btnclk("*")).grid(row=2,column=3)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

b1=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="1", bg="grey", command=lambda:btnclk(1)).grid(row=3,column=0)

b2=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="2", bg="grey", command=lambda:btnclk(2)).grid(row=3,column=1)

b3=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="3", bg="grey", command=lambda:btnclk(3)).grid(row=3,column=2)

bm=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="-", bg="grey", command=lambda:btnclk("-")).grid(row=3,column=3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bd=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="/", bg="grey", command=lambda:btnclk("/")).grid(row=4,column=0)

b0=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="0", bg="grey", command=lambda:btnclk(0)).grid(row=4,column=1)

be=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="=", bg="grey", command=btneq).grid(row=4,column=2)

bs=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="+", bg="grey", command=lambda:btnclk("+")).grid(row=4,column=3)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bdot=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text=".", bg="grey", command=lambda:btnclk(".")).grid(row=4,column=4)

bop=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text="(", bg="grey", command=lambda:btnclk("(")).grid(row=3,column=4)

bcp=Button(root, padx=16, pady=16, bd=6, fg="White", font=("arial",20,"bold"), text=")", bg="grey", command=lambda:btnclk(")")).grid(row=2,column=4)

bq=Button(root, padx=14, pady=14, bd=6, fg="White", font=("arial",20,"italic"), text="off", bg="grey", command=root.destroy).grid(row=1,column=4)


root.mainloop()
