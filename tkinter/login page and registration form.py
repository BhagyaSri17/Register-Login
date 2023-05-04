import mysql.connector as mc
from tkinter import *
from tkinter import messagebox
import re
con=mc.connect(host='localhost',user='root',password='root',database='login')
cur=con.cursor()
def submit():     #submit button
    fname=firstname.get()
    lname=lastname.get()
    sid=userid.get()
    pwd=Password.get()
    cpwd=Cpassword.get()
    phno=Phoneno.get()
    address=Address.get()
    Gender=gender.get()
    unique="select * from register where userid=%s"
    cur.execute(unique,[userid.get()])
    res=cur.fetchone()
    x=re.search("^[0-9]{10}$",phno)# for phone number verification
    y=re.search("^(.{8})",pwd)#for password verification
    if  userid.get()=="" or firstname.get()=="" or Password.get()=="" or Cpassword.get()=="" :
        messagebox.showerror('Error','All fieid are required')
    elif Password.get()!=Cpassword.get():
        messagebox.showerror('Error','PassWord Mismatch')
    elif y==None:
        messagebox.showerror('Error','Password should have atleast 8 characters')
    elif (c1.get() or c2.get() or c3.get())==0:
        messagebox.showerror('Error','Select the Course')
    elif res!=None:
        messagebox.showerror('Error','Userid Already Exist')
    elif x==None:
        messagebox.showerror('Error','Enter Correct Phone Number')
    else:
        s="insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)"
        t=(fname,lname,sid,pwd,cpwd,','.join(value),phno,Gender)
        cur.execute(s,t)
        con.commit()
        messagebox.showinfo('Registration','Successful')
        reg.destroy
def reg():       #register button
    global reg
    reg=Toplevel(win)
    reg.title('Registration Form')
    reg.geometry('500x500+500+250')
    l1=Label(reg,text='First name:').grid(row=0,column=0,pady=10,padx=5)
    l2=Label(reg,text='Last Name:').grid(row=1,column=0,pady=10,padx=5)
    l3=Label(reg,text='User id:').grid(row=2,column=0,pady=10,padx=5)
    l4=Label(reg,text='Password:').grid(row=3,column=0,pady=10,padx=5)
    l5=Label(reg,text='Confirm password:').grid(row=4,column=0,pady=10,padx=5)
    l6=Label(reg,text='Phone no:').grid(row=5,column=0,pady=10,padx=5)
    global firstname, lastname,userid, Password,Cpassword, Phoneno, Address,gender
    firstname=StringVar()
    lastname=StringVar()
    Password=StringVar()
    Cpassword=StringVar()
    Address=StringVar()
    gender=StringVar()
    userid=StringVar()
    Phoneno=StringVar()
    t1=Entry(reg,textvariable=firstname).grid(row=0,column=1)
    t2=Entry(reg,textvariable=lastname).grid(row=1,column=1)
    t3=Entry(reg,textvariable=userid).grid(row=2,column=1)
    t4=Entry(reg,textvariable=Password,show="*").grid(row=3,column=1)
    t5=Entry(reg,textvariable=Cpassword,show="*").grid(row=4,column=1)
    t6=Entry(reg,textvariable=Phoneno).grid(row=5,column=1)
    l7=Label(reg,text="select the courses:").grid(row=10,column=0)   # for checkbuttons
    def check():
        global value
        value=[]
        if c1.get():
            value.append('python')
        if c2.get():
            value.append('java')
        if c3.get():
            value.append('cpp')
    global c1,c2,c3
    c1=IntVar()
    c2=IntVar()
    c3=IntVar()
    Checkbutton(reg,text='Python',variable=c1).grid(row=10,column=1)
    Checkbutton(reg,text='java',variable=c2).grid(row=10,column=2)
    Checkbutton(reg,text='c++',variable=c3).grid(row=10,column=3)
    click=Button(reg,text="Select",command=check)
    click.grid(row=12,column=2)
    r=IntVar()   #radio buttons
    def fun():
        if gender.get()=="Male":
            sel='you selected:Male'
        if gender.get()=="Female":
            sel="you selected:Female"
        rb.config(text=sel)
    Label(reg,text="Select Gender:").grid(row=6,column=0)
    r1=Radiobutton(reg,text='Male',variable=gender,value='Male',command=fun)
    r1.grid(row=6,column=1)
    r2=Radiobutton(reg,text='Female',variable=gender,value='Female',command=fun)
    r2.grid(row=6,column=2)
    rb=Label(reg)
    rb.grid(row=7,column=1)
    Button(reg,text='submit',bd=3,command=submit).grid(row=20,column=1)
    Button(reg,text='cancel',bd=3,command=reg.destroy).grid(row=20,column=2)
    reg.mainloop()
def logged():
    global log
    log=Toplevel(win)
    log.title('Details')
    log.geometry('300x300+500+250')
    Label(log,text="Welcome!",font="TimesNewRoman 15 bold").pack() 
    s="select f_name,l_name from register where userid=%s"
    cur.execute(s,[Userid.get()])
    res=cur.fetchone()
    Label(log,text=res).pack()
    Label(log,text="You Have Successfully logged in").pack() 
    Label(log,text="Thank you!",font="arial 10 bold").pack()
    global photo
    photo=PhotoImage(file=r"C:\Users\bhagy\Downloads\shin (4).png")
    Label(log,image=photo).pack()
def logging():
    s="select * from register where userid=%s and Pwd=%s"
    cur.execute(s,[Userid.get(),PassWord.get()])
    res=cur.fetchall()
    if res:
        logged()
    else:
        messagebox.showinfo('warning','info is wrong')
win=Tk()
win.title('Login page')
win.geometry('300x300')
l1=Label(win,text='UserId:').grid(row=0,column=0,pady=10,padx=5)
l2=Label(win,text='Password:').grid(row=1,column=0,pady=10,padx=5)
Userid=Entry(win)
Userid.grid(row=0,column=1)
PassWord=Entry(win,show="*")
PassWord.grid(row=1,column=1)
register=Button(win,text='Register',bg='white',command=reg).grid(row=5,column=1)
btn=Button(win,text='login',bg='white',command=logging).grid(row=5,column=0)
win.mainloop()
