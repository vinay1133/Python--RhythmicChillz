from tkinter import *
from email import message
# from MySQLdb import *
from tkinter import messagebox
welcome=Tk()
welcome.title("Welcome Screen")
welcome.geometry("1199x600+100+50")
#-----BG Image------
bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Welcome_final.png")
bg_image=Label(welcome,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
label=Label(welcome,text="Welcome to RhythmicChillz!",font=("Impact",35),fg="#d77337",bg="#3B4B64").place(x=90,y=70)
#-----Buttons--------
def music():
    welcome.destroy()
    import MusicPlayer
def podcast():
   welcome.destroy()
   import Podcast
btn_music=Button(welcome,text="Music",bg="#d77337",fg="white",font=("times new roman",20,"bold"),command=music).place(x=750,y=240,width=180,height=40)
btn_podcast=Button(welcome,text="Podcast",bg="#d77337",fg="white",font=("times new roman",20,"bold"),command=podcast).place(x=750,y=300,width=180,height=40)
welcome.mainloop()