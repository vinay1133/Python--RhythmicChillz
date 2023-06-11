from tkinter import *

Podcast=Tk()
Podcast.geometry("1199x600")
Podcast.title("Podcast")
bg=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Podcast resize.png")
bg_image=Label(Podcast,image=bg).place(x=0,y=0)

photo1 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\R&S B.png")
btn=Button(Podcast, image = photo1, bd=0).place(x=51,y=169)

def sm_window():
    Podcast.destroy()
    import Podcast_SM
photo2 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\SM B.png")
btn=Button(Podcast, image = photo2, bd=0,command=sm_window).place(x=51,y=309)

photo3 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\H B.png")
btn=Button(Podcast, image = photo3, bd=0).place(x=51,y=460)

def suc_window():
    Podcast.destroy()
    import Podcast_SC
photo4 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\SUC B.png")
btn=Button(Podcast, image = photo4, bd=0,command=suc_window).place(x=430,y=169)

photo5 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Art B.png")
btn=Button(Podcast, image = photo5, bd=0).place(x=430,y=309)

def gni_window():
    Podcast.destroy()
    import Podcast_GNI
photo6 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\\GNI B.png")
btn=Button(Podcast, image = photo6, bd=0,command=gni_window).place(x=430,y=460)

photo7 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Tech B.png")
btn=Button(Podcast, image = photo7, bd=0).place(x=815,y=169)

photo8 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Edu B.png")
btn=Button(Podcast, image = photo8, bd=0).place(x=814,y=309)

photo9 = PhotoImage(file = "C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\Buss B.png")
btn=Button(Podcast, image = photo9, bd=0).place(x=814,y=460)

def wlcm_window():
    Podcast.destroy()
    import Welcome
Back=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\previous.png")
back_btn=Button(Podcast,image=Back,fg="white",bg="#29374B",bd=0,command=wlcm_window).place(x=420,y=25)

Podcast.mainloop()

