import sqlite3
with sqlite3.connect("questions.db") as db:
    cursor=db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS interview_question(
number_questions integer PRIMARY KEY,
question text NOT NULL,
answer text NOT NULL)""")
cursor.execute("""INSERT INTO interview_question("number_questions","question","answer")
VALUES("1","Что такое git ?","Git - это распределенная система управления версиями")""")
db.commit()