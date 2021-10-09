from Tkinter import*

root=Tk()

root.title("calculator")
#root.geometry("300x530")
root.minsize(300,530)
root.maxsize(300,530)
root.configure(background='black')

#------------------------------------------------------------------------
operator=""
def click(number):
    global operator
    operator=operator+str(number)
    txt_input.set(operator)
    
def  clear():
    global operator
    operator=""
    txt_input.set(operator)

def  save():
    global operator
    calculation=  str(eval(operator))
    txt_input.set(calculation)
    operator=""
    
txt_input=StringVar()

e=Entry(root,fg='white',font=('Old English Text MT',30),bg=("black"),bd=2,textvariable=txt_input)
e.place(x=10,y=5,width=270)
#------------------------------------------------------------------------
b1=Button(root,text='C',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:clear(),bd=7)
b1.place(x=10,y=70,width=50)

b2=Button(root,text='/',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('/'),bd=7)   
b2.place(x=80,y=70,width=50)

b3=Button(root,text='%',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('%'),bd=7)
b3.place(x=150,y=70,width=50)

b4=Button(root,text='^',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('^'),bd=7)
b4.place(x=220,y=70,width=50)
#-------------------------------------------------------------------------
b5=Button(root,text='1',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(1),bd=7)
b5.place(x=10,y=140,width=50)

b6=Button(root,text='2',fg='black',font=('freestyle script',22),bg='yellow',command=lambda:click(2),bd=7)
b6.place(x=80,y=140,width=50)

b7=Button(root,text='3',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(3),bd=7)
b7.place(x=150,y=140,width=50)

b8=Button(root,text='*',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('*'),bd=7)
b8.place(x=220,y=140,width=50)
#-------------------------------------------------------------------------
bMINUS=Button(root,text='4',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(4),bd=7)
bMINUS.place(x=10,y=210,width=50)

bPLUS=Button(root,text='5',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(5),bd=7)
bPLUS.place(x=80,y=210,width=50)

bMUL=Button(root,text='6',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(6),bd=7)
bMUL.place(x=150,y=210,width=50)

bDIV=Button(root,text='-',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('-'),bd=7)
bDIV.place(x=220,y=210,width=50)
#-------------------------------------------------------------------------l
bDOU=Button(root,text='7',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(7),bd=7)
bDOU.place(x=10,y=280,width=50)

bZERO=Button(root,text='8',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(8),bd=7)
bZERO.place(x=80,y=280,width=50)

bPOINT=Button(root,text='9',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(9),bd=7)
bPOINT.place(x=150,y=280,width=50)

bEQUAL=Button(root,text='+',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('+'),bd=7)
bEQUAL.place(x=220,y=280,width=50)
#---------------------------------------------------------------------------
bPOS=Button(root,text='00',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click("00"),bd=7)
bPOS.place(x=10,y=350,width=50)

bBRA=Button(root,text='0',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click(0),bd=7)
bBRA.place(x=80,y=350,width=50)

bC=Button(root,text='.',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:click('.'),bd=7)
bC.place(x=150,y=350,width=50)

bX=Button(root,text='=',fg='black',font=('Old English Text MT',22),bg='yellow',command=lambda:save(),bd=7)
bX.place(x=220,y=350,width=50)
#@-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bPOS=Button(root,text='±',fg='black',font=('Old English Text MT',18),bg='yellow',command=lambda:click("±"),bd=7)
bPOS.place(x=10,y=430,width=80)

bBRA=Button(root,text='log',fg='black',font=('Old English Text MT',18),bg='yellow',command=lambda:click('log('),bd=7)
bBRA.place(x=110,y=430,width=80)

bC=Button(root,text='⌫',fg='black',font=('Old English Text MT',18),bg='yellow',command=lambda:clear(),bd=7)
bC.place(x=200,y=430,width=80)

#-------------------------------------------------------------------------
L=Label(root,text=".........made by prince  .........",font=("Pristina",20),fg='white',bg='black')
L.place(x=20,y=490)



root.mainloop()
