import tkinter as tk
from tkinter import *
def display(list,flag):
    l1.pack()
    t1.delete(1.0,END)
    for item in list:
        t1.insert(INSERT,item)
        t1.insert(INSERT,'\n')
    t1.pack()
root=tk.Tk()

m1=Menubutton(root,text="other news",relief=RAISED,anchor=NW)
m1.menu = tk.Menu(m1, tearoff=0)
m1['menu'] = m1.menu
m1.menu.add_command(label="headline",command=lambda:display(list1,1))
m1.menu.add_command(label="news for you",command=lambda:display(list2,1))
m1.menu.add_command(label="Local News",command=lambda:display(list3,1))
m1.pack()
list1=['n1','n2','n3']
list2=['n11','n12','n13']
list3=['n21','n22','n23']
l1=Label(root,text="news")
t1=Text(root)
display(list1,0)
root.mainloop()
