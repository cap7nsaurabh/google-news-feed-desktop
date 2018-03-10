import tkinter as tk
from tkinter import *
def display(list,root):
    l1=Label(root,text="news")
    l1.pack()
    t1=Text(root)
    for item in list:
        t1.insert(INSERT,item)
        t1.insert(INSERT,'\n')
    t1.pack()
root=tk.Tk()
list=['i','love','you']
display(list,root)
root.mainloop()
