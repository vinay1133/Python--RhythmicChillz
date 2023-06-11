from tkinter import *
root=Tk()
root.geometry("600x600")
root.config(bg='white')
root.title('Light_Dark')
button_mode=True
def change():
    global button_mode
    if button_mode:
        button.config(image=light,bg='#26242f',activebackground='#26242f')
        root.config(bg='#26242f')
        button_mode=False
    else:
        button.config(image=dark,bg='white',activebackground='white')
        root.config(bg='white')
        button_mode=True
light=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\light.png")
dark=PhotoImage(file="C:\\Users\\Vinay Bhojwani\\AppData\\Local\\Programs\\Python\\Python39\\SBL_MiniProject\\Images\\dark.png")
button=Button(root,image=dark,bg='white',activebackground='white',command=change)
label=Label(text='Hey there!',fg='cyan',bg='black',font=("Arial 16 bold"))
label.pack(padx=20,pady=50)
button.pack(padx=40,pady=100)
root.mainloop()
