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
    i=0
    for item in list:
        list2.append(item.get_text())
        i=i+1
        if i==20:
            break
    return list2
def display(list,root,var):
    l1=Label(root,text=var)
    l1.pack()
    line="---------------------------------------------\n"
    t1=Text(root,wrap=WORD)
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
display(list2,root,tit1)
root.mainloop()
