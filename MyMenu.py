from tkinter import *

root = Tk()
root.title("Backup Menu")
root.geometry("450x450")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)








root.mainloop()
