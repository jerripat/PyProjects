
from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.geometry("450x450")


def radio():
    if v.get() == 1:
        my_label = Label(root, text="You clicked button one").pack(pady=10)
    elif v.get() == 2:
        my_label = Label(root, text="You clicked button Two",
                         fg="red").pack(pady=10)
    elif v.get() == 3:
        my_label = Label(root, text="You clicked button Three").pack(pady=10)
    else:
        my_label = Label(root, text="You clicked button Four",
                         fg="green").pack(pady=10)


def menu_choice():
    if v.get() == "rsync all files":
        my_label =Label(root, text="You slected all files?")
    else:
        my_label = Label(root,"Make another selection")
    my_label = Label(root, text=v.get())
    my_label.pack(pady=10)


# Radio Buttons
v = IntVar()
v.set(1)
#x = StringVar()
rbutton_1 = Radiobutton(root, text="One", variable=v, value=1).pack()
rbutton_2 = Radiobutton(root, text="Two", variable=v, value=2).pack()
rbutton_3 = Radiobutton(root, text="Three", variable=v, value=3).pack()
rbutton_4 = Radiobutton(root, text="Four", variable=v, value=4).pack()

my_button = Button(root, text="Click me!", command=radio)
my_button.pack(pady=10)

# Check boxs

v = StringVar()
my_check = Checkbutton(root, text="rsync all files", variable=v,
                       onvalue="rsync all files", offvalue="none")
my_check.deselect()
my_check.pack()

my_button = Button(root, text="Select backup",
                   command=menu_choice).pack(pady=20)


root.mainloop()
