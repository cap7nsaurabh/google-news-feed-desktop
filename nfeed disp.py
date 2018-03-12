from bs4 import BeautifulSoup as bs
import urllib.request as u2
import tkinter as tk
from tkinter import *
def getdata(str):
    url=str;
    req=u2.urlopen(url)
    soup=bs(req,"html.parser")
    list=[]
    list2=[]
    list=soup.find_all('a',class_="nuEeue hzdq5d ME7ew")
    for item in list:
        list2.append(item.get_text())        
    return list2
def display(list,stre):
    var=stre
    l1.pack()
    t1.delete(1.0,END)
    line="---------------------------------------------\n"
    for item in list:
        t1.insert(INSERT,item)
        t1.insert(INSERT,'\n')
        t1.insert(INSERT,line)
    t1.pack()
root=tk.Tk()
strhead="https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
strlocal="https://news.google.com/news/local?hl=en-IN&gl=IN&ned=in"
strforyou="https://news.google.com/news/sfy?hl=en-IN&gl=IN&ned=in"
list2=getdata(strhead)
list3=getdata(strlocal)
list4=getdata(strforyou)
tit1="Headlines"
tit2="News for you"
tit3="Local news"
m1=Menubutton(root,text="other news",relief=RAISED,anchor=NW)
m1.menu = tk.Menu(m1, tearoff=0)
m1['menu'] = m1.menu
m1.menu.add_command(label="headline",command=lambda:display(list2,tit1))
#m1.menu.add_command(label="news for you",command=lambda:display(list3,tit2))
m1.menu.add_command(label="Local News",command=lambda:display(list3,tit3))
m1.pack()
var=StringVar()
l1=Label(root,textvariable=var)
t1=Text(root,wrap=WORD)
display(list2,tit1)
root.mainloop()
