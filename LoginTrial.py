from cmath import log10
from email import message
from tkinter import *
from MySQLdb import *
from tkinter import messagebox
from PIL import *
from PIL import ImageTk
from PIL import Image
# def alert(title, message, kind='info', hidemain=True):
#     if kind not in ('error', 'warning', 'info'):
#         raise ValueError('Unsupported alert kind.')

#     show_method = getattr(messagebox, 'show{}'.format(kind))
#     show_method(title, message)
def img1(root):
    global img 
    img = ImageTk.PhotoImage(Image.open("SBL_MiniProject\\bg.png"))
    l1=Label(root,image=img)
    l1.place(relx=0.5,rely=0.5,anchor=CENTER)
    # l1.pack()
def trial(root):
    print('hi')
    login1=LabelFrame(root)
    # login1.config(title="Login_Screen")
    # login1.geometry("1199x600+100+50")
    # img1(root)
    #-----BG Image------
    # bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\bg.png") 
    # bg_image=Label(login1,image=bg).place(relx=0.5,rely=0.5,anchor=CENTER)
    #----Login Frame----
    frame_login=Frame(login1,bg="white")
    # frame_login.place(x=350,y=40,height=327,width=500)
    frame_login.pack()
    title=Label(frame_login,text="Login Here",font='Impact 35 bold',fg="#3B4B64",bg="white").grid(row=0,column=0,columnspan=2)
    desc=Label(frame_login,text="Enter to music world",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").grid(row=1,column=0,columnspan=2)
    print('hello')
    lbl_user=Label(frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").grid(row=2,column=0)
    txt_user=Entry(frame_login,font=("times new roman",15),bg="lightgray")
    txt_user.grid(row=2,column=1)

    '''lbl_pass=Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").place(x=60,y=190)
    txt_pass=Entry(frame_login,font=("times new roman",15),bg="lightgray")
    txt_pass.config(show='*')
    txt_pass.place(x=70,y=220,width=350,height=35)
    forgotpass1=Button(frame_login,text="Forgot Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12,'italic'),command=lambda: forgotpass(login1,txt_user,txt_pass))
    forgotpass1.place(x=55,y=260)
    login_btn=Button(login1,text="Login",fg="White",bg="#d77337",font=("times new roman",20,"bold"),command=lambda: check(login1,txt_user,txt_pass)).place(x=530,y=320,width=180,height=40)'''
    login1.pack()

#Checking Credentials
def check(login1,txt_user,txt_pass):
    c=connect('localhost','root','Bappamorya@1133','sbl_mp')
    mycursor=c.cursor()
    uname=txt_user.get()
    pas=txt_pass.get()
    sql='select * from signup where Username = %s and Password = %s'
    mycursor.execute(sql,[uname,pas])
    row=mycursor.fetchall()
    if row:
        messagebox.showinfo("Congratulations","Login Successful!")
        login1.destroy()
    elif uname=='' or pas=='':
        messagebox.showwarning("Warning","Kindly enter all the fields")
    else:
        messagebox.showerror("Error","Invalid Username or Password")
    c.close()

#Forgot Password Window
def forgotpass(login1,txt_user1,txt_pass1):
    login1.destroy()
    fpass=Tk()
    fpass.title("Forgot Passoword")
    fpass.geometry("1199x600+100+50")
    #-----BG Image------
    bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\bg.png") 
    bg_image=Label(fpass,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
    #----Login Frame----
    frame_fpass=Frame(fpass,bg="white")
    frame_fpass.place(x=350,y=40,height=327,width=500)
    title=Label(frame_fpass,text="New Credentials",font='Impact 35 bold',fg="#3B4B64",bg="white").place(x=120,y=20)
    desc=Label(frame_fpass,text="Enter new credentials here",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=150,y=80)

    lbl_user1=Label(frame_fpass,text="Your Username",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").place(x=60,y=110)
    txt_user1=Entry(frame_fpass,font=("times new roman",15),bg="lightgray")
    txt_user1.place(x=70,y=140,width=350,height=35)

    lbl_pass1=Label(frame_fpass,text="New Password",font=("Goudy old style",15,"bold"),fg="#3B4B64",bg="white").place(x=60,y=190)
    txt_pass1=Entry(frame_fpass,font=("times new roman",15),bg="lightgray")
    txt_pass1.config(show='*')
    txt_pass1.place(x=70,y=220,width=350,height=35)
    submit_btn=Button(fpass,text="Submit",fg="White",bg="#d77337",font=("times new roman",20,"bold"),command=newcred).place(x=530,y=320,width=180,height=40)
    fpass.mainloop()

    #Updating credentials

def newcred(fpass,txt_user1,txt_pass1):
    c=connect('localhost','root','Bappamorya@1133','sbl_mp')
    mycursor=c.cursor()
    uname=txt_user1.get()
    query="select * from signup where Username=%s"
    mycursor.execute(query,[uname])
    result=mycursor.fetchall()
    if not result:
        messagebox.showerror("Error","User doesn't exist...")
    else:
        messagebox.showinfo("Info","User verified...")
        npas=txt_pass1.get()
        if npas=='':
            messagebox.showerror("Error","Please enter password...")
        else:
            sql="update signup set Password=%s where Username=%s"
            mycursor.execute(sql,[npas,uname])
            messagebox.showinfo("Success","Password Ressetted...")
    c.commit()
    c.close()

#login1.mainloop()