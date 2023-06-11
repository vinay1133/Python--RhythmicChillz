from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root=Tk()
root.title("Podcast: StandUp Comedy")
root.geometry("1199x600+100+50")
bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Music_Final.png")
bg_image=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
root.resizable(False,False)

mixer.init()

def open_folder():
    path="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Podcasts\\StandUp Comedy"
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

#icon
image_icon=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\logo.png")
root.iconphoto(False,image_icon)

#Label
btn_container=Label(root,text="",font=("times new roman",15),fg="white",bg="Black",bd=2).place(x=250,y=180,width=300,height=250)

#button
play_button=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\play.png")
Button(root,image=play_button,bg="black",bd=0,command=play_song).place(x=350,y=200)

stop_button=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\stop.png")
Button(root,image=stop_button,bg="black",bd=0,command=mixer.music.stop).place(x=280,y=300)

resume_button=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\resume.png")
Button(root,image=resume_button,bg="black",bd=0,command=mixer.music.unpause).place(x=365,y=300)

pause_button=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\pause.png")
Button(root,image=pause_button,bg="black",bd=0,command=mixer.music.pause).place(x=450,y=300)

#label
music=Label(root,text="",font=("arial",15),fg="white",bg="#7C8EAD")
music.place(x=382,y=450,anchor="center")

#music
Menu=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\menu.png")
Label(root,image=Menu,bg="#29374B").pack(padx=10,pady=50,side=RIGHT)

music_frame= Frame(root,bd=2,relief=RIDGE)
music_frame.place(x=615,y=205,width=560,height=250)

Button(root,text="Explore Podcast",width=15,height=2,font=("Sans Serif",12,"bold"),fg="white",bg="#D77337",command=open_folder).place(x=620,y=135)

scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("Sans Serif",15),bg="#29374B",fg="white",selectbackground="#7C8EAD",cursor="hand2",bd=0,yscrollcommand=scroll.set)

scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT,fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

def wlcm_window():
    root.destroy()
    import Podcast
Back=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\previous.png")
back_btn=Button(root,image=Back,fg="white",bg="#29374B",bd=0,command=wlcm_window).place(x=60,y=450)
root.mainloop()