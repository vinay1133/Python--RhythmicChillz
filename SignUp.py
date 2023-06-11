from tkinter import *
from email import message
from MySQLdb import *
from tkinter import messagebox
signup=Tk()
signup.title("Signup Screen")
signup.geometry("1199x600+100+50")

#-----BG Image------
bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\bg.png")
bg_image=Label(signup,image=bg).place(x=0,y=0,relwidth=1,relheight=1)

#----signup Frame----
frame_signup=Frame(signup,bg="white")
frame_signup.place(x=350,y=20,height=370,width=500)
title=Label(frame_signup,text="Sign Up",font=("Impact",35,"bold"),fg="#3B4B64",bg="white").place(x=170,y=5)
label=Label(frame_signup,text="Already have an account?",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=70)

lbl_user=Label(frame_signup,text="Username",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").place(x=60,y=100)
txt_user=Entry(frame_signup,font=("times new roman",15),bg="lightgray")
txt_user.place(x=70,y=130,width=350,height=35)

lbl_pass=Label(frame_signup,text="Password",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").place(x=60,y=180)
txt_pass=Entry(frame_signup,font=("times new roman",15),bg="lightgray")
txt_pass.config(show='*')
txt_pass.place(x=70,y=210,width=350,height=35)

lbl_name=Label(frame_signup,text="Enter your Name",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=60,y=260)
txt_name=Entry(frame_signup,font=("times new roman",15),bg="#3B4B64",fg="white")
txt_name.place(x=70,y=290,width=350,height=35)
def eye1():
    txt_pass.config(show='')
eye=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\view.png")
b=Button(frame_signup,image=eye,command=eye1,bd=0,bg='white').place(x=440,y=200)
#Checking Credentials
def add():
    c=connect('localhost','root','Bappamorya@1133','sbl_mp')
    mycursor=c.cursor()
    uname=txt_user.get()
    pas=txt_pass.get()
    name=txt_name.get()
    sql='insert into signup VALUES (%s,%s,%s)'
    mycursor.execute(sql,[uname,pas,name])
    messagebox.showinfo("Welcome","You are successfully signed in!!")
    c.commit()
    c.close()
    messagebox.showinfo("Info","Let's Login...")
    signup.destroy()
    import Login
#forget=Button(frame_signup,text="Forget Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=60,y=260)
signup_btn=Button(signup,text="Sign Up",fg="White",bg="#d77337",font=("times new roman",20,"bold"),command=add).place(x=510,y=370,width=180,height=40)
def loginn_window():
    signup.destroy()
    import Login
signin_btn=Button(frame_signup,text="Sign in",command=loginn_window,font=("Goudy old style",15,"bold"),bd=0,fg="#3B4B64",bg="white").place(x=310,y=67)
signup.mainloop()