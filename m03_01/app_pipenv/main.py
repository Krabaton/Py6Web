from tkinter import Tk, Label, Button, Entry


def handler():
    text = txt.get()
    txt.delete(0, 'end')
    lbl.configure(text=text)


wnd = Tk()

wnd.title('My App')
wnd.geometry('800x600')
wnd.resizable(False, False)

lbl = Label(wnd, text='Hello world!', font=('Arial', 20), fg='#0DCA1B')
lbl.place(x=40, y=30)

btn1 = Button(wnd, text='Close', font=('Courier', 16), command=wnd.destroy)
btn1.place(x=40, y=100, width=150, height=45)

txt = Entry(wnd, width=30, font=('Arial', 20))
txt.place(x=40, y=150)

btn2 = Button(wnd, text='Ok', font=('Courier', 16), command=handler)
btn2.place(x=40, y=200, width=150, height=45)

wnd.mainloop()
