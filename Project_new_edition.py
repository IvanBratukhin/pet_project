
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import sqlite3
window=Tk()
window.title("Вопросы к собеседованию ")
window.geometry("450x100")
def click():
    root=tk.Tk()
    root.title("Вопросы")
    root.geometry("1500x1500")
    tree=ttk.Treeview(root, column=("c1","c2","c3"), show="headings")
    tree.column("#1",anchor=tk.CENTER)
    tree.heading("#1",text="Номер вопроса")
    tree.column("#2",anchor=tk.CENTER)
    tree.heading("#2", text="Вопрос")
    tree.heading("#3",text="Ответ")
    tree.pack()
    con1=sqlite3.connect("questions.db")
    cur1=con1.cursor()
    cur1.execute("SELECT *FROM interview_question")
    rows=cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("",tk.END,values=row)
    con1.close()
    
button1=Button(text="Let's go!", command= click)
button1.place(x=50,y=20,width=100, height=25)# попробуй grid


















window.mainloop()