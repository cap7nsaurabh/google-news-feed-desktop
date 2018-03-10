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
def display(list,root):
    t1=Text(root)
    for item in list:
        t1.insert(INSERT,item)
        t1.insert(INSERT,'\n')
    t1.pack()
root=tk.Tk()
strhead="https://news.google.com/news/?ned=in&gl=IN&hl=en-IN"
strlocal="https://news.google.com/news/local?hl=en-IN&gl=IN&ned=in"
strforyou="https://news.google.com/news/sfy?hl=en-IN&gl=IN&ned=in"
list2=getdata(strhead)
list3=getdata(strlocal)
list4=getdata(strforyou)
display(list2,root)
root.mainloop()
