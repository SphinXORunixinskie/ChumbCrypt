from tkinter import *

def show():
    p = password.get()
    print(p)

app = Tk()

username = StringVar()
password = StringVar()
GPGPath  = StringVar()

userEntry = Entry(app, textvariable=username).pack()
passEntry = Entry(app, textvariable=password, show='*').pack()
GPGEntry  = Entry(app, textvariable=GPGPath).pack()
submit = Button(app, text='Login', command=show).pack()
app.mainloop()
