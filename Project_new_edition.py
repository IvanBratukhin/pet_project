from tkinter import *
from textwrap import wrap
import tkinter as tk
import sqlite3
window=Tk()
window.title("Вопросы к собеседованию ")
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
w=w//2
h=h//2
w=w-200
h=h-200
window.geometry(f"450x100+{w}+{h}")
def click():
    questions_editor=Text(height=5,wrap="word")
    questions_editor.pack(anchor=N,fill=X)
    word_editor=Text(height=5,wrap="word")
    word_editor.pack(anchor=S,fill=X)
    with sqlite3.connect("C:\Python\pet_project\pet_project\questions.db") as db:
        cursor=db.cursor()
        cursor.execute("SELECT question FROM interview_question")
    for rows in cursor.fetchall():
        print(rows)
        questions_editor.insert("1.0",*rows)
    db.close()

                         

   
    
button1=Button(text="Let's go!", command= click)
button1.place(x=50,y=20,width=100, height=25)# попробуй grid


















window.mainloop()