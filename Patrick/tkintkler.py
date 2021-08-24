from tkinter import *

window = Tk()
lbl = Label(window,
            text="Внизу, блядь, кнопка ! ",
            fg='green',
            font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld = Entry(window, text="This is Entry Widget", bd=3)
txtfld.place(x=90, y=150)

btn = Button(window, text="BUTTON", fg='gray')

btn.place(x=90, y=100)

window.title('Hope you will work')
window.geometry("300x200+10+20")
window.mainloop()
