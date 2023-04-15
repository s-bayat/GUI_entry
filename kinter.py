from tkinter import *

root = Tk()
root.title("Entry")
root.geometry("400x400")
root.resizable(height=False, width=False)

label = Label(root, text="please write your name:")
label.place(x=20, y=20)
inputName = Entry(root)
inputName.place(x=22, y=60)


def get_name():
    print(inputName.get())


btn = Button(root, text="submit", command=lambda :get_name())
btn.place(x=20, y=90)

root.mainloop()
