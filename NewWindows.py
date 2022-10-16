from tkinter import *

root = Tk()
root.title("New Windows")
root.geometry("450x550")


def newWindow():
    new = Toplevel()
    new.title("Second window Windows")
    new.geometry("300x350")
    my_label = Label(new, text="This is a new window").pack(pady=20)
    new.mainloop()


# Create new window
my_button = Button(root, text="Open new window", command=newWindow)
my_button.pack(pady=10)


root.mainloop()
