import sqlite3
with sqlite3.connect("C:\Python\pet_project\pet_project\questions.db") as db:
    cursor=db.cursor()
cursor.execute("SELECT * FROM interview_question")
for i in cursor.fetchall():
    print(i)
db.close()