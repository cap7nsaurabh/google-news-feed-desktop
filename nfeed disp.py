import tkinter as tk
from tkinter import *
def display(list,root,flag):
    l1=Label(root,text="news")
    l1.pack()
    t1=Text(root)
    t1.delete(1.0,END)
    for item in list:
        t1.insert(INSERT,item)
        t1.insert(INSERT,'\n')
    t1.pack()
    b1=Button(root,text="clear",command=lambda: t1.delete(1.0,END))
    b1.pack()
root=tk.Tk()
m1=Menubutton(root,text="other news",relief=RAISED,anchor=NW)
h=IntVar()
nfy=IntVar()
ln=IntVar()
m1.menu = tk.Menu(m1, tearoff=0)
m1['menu'] = m1.menu
m1.menu.add_command(label="headline",command=lambda:display(list1,root,1))
m1.menu.add_command(label="news for you",command=lambda:display(list2,root,1))
m1.menu.add_command(label="Local News",command=lambda:display(list3,root,1))
m1.pack()
list1=['n1','n2','n3']
list2=['n11','n12','n13']
list3=['n21','n22','n23']
display(list1,root)
root.mainloop()
