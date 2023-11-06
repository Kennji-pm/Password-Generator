from tkinter import *
from tkinter import messagebox
from datetime import datetime
import random

lower_case = "qwertyuiopasdfghjklzxcvbnm"
upper_case = lower_case.upper()
numbers = str(1234567890)
symbols = "!@#$%^&*()=+"
now = datetime.now()

all = lower_case + upper_case + numbers + symbols

root = Tk()
root.minsize(width=500, height=200)
root.maxsize(width=600, height=250)
root.title("Password Generator")
root.iconbitmap("password_gen.ico")
Label(root, text="Code by Kennji").pack(side=BOTTOM)

frame = Frame(root)
frame.pack()

def close_app():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def writetofile(pw):
    dt = now.strftime("%d/%m/%Y")
    print(dt + " New password to saved!")
    f = open("Password.txt", "a", encoding="utf8")
    f.write(dt + " | " + pw + "\n")
    f.close

def run():
    line = int(length.get())

    if line <= 20 and line > 0:
        yp.config(text="Your Password (" + str(line) + " Length)", width=20)
        pw = "".join(random.sample(all, line))
        line = pw
        writetofile(pw)
        root.clipboard_clear()
        root.clipboard_append(line)
        root.update()
        listbox.delete(0, END)
        listbox.insert(END, line)
        messagebox.showinfo("Password Generator", "Your Password Has Been Copied!")
    elif line == 0:
        line = "Enter Password Length!"
        listbox.delete(0, END)
        listbox.insert(END, line)
        yp.config(text="Your Password", width=15)
    else:
        line = "Max length is 20, try again!"
        listbox.delete(0, END)
        listbox.insert(END, line)
        yp.config(text="Your Password", width=15)

mainframe = LabelFrame(frame, text="PASSWORD GENERATOR")
mainframe.grid(row=0, column=0, pady=10)
#Label(root, text="PASSWORD GENERATOR", fg="black", font=("SDK_JP_Web", 12), width=21).grid(row=0)
Label(mainframe, text="Password Length", width=15).grid(row=1, column=0, padx=15, pady=15)
length = StringVar()
Spinbox(mainframe, from_=0, to='infinity', textvariable=length).grid(row=1, column=1)

button=Frame(mainframe)
Button(button, text="Generator", command=run).pack(side=LEFT)
button.grid(row=1, column=2, padx=20)

for widget in mainframe.winfo_children():
    widget.grid_configure(padx=20, pady=5)

courses_frame = LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", pady=30)

yp = Label(courses_frame, text="Your Password", width=15)
yp.grid(row=0, column=0, padx=20)
listbox = Listbox(courses_frame, width=30, height=1)
listbox.grid(row=0, column=1, padx=10, pady=10)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=20, pady=5)

root.bind("<Escape>", lambda x: root.destroy())
root.bind("<Return>", lambda x: run())
root.protocol("WM_DELETE_WINDOW", close_app)
root.mainloop()