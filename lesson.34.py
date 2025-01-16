import sqlite3
db = sqlite3.connect('example.db')
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS pupils(
              number INTEGER,
              name TEXT,
              surname TEXT,
              phone_num TEXT,
              age INTEGER)
''')
# cursor.execute('''
# INSERT INTO pupils(
#                number,name,surname,phone_num,age)
#                VALUES(3,'Azamat','+998911234567',13)

# ''')
# db.commit()#save-сохранить

num = int(input('san jaz:'))
name = input('atin jaz:')
surname=input('familiaysin jaz:')
phone= input('nomerin jaz:')
age = int(input('jasin jaz:'))

cursor.execute('''
INSERT INTO pupils(
               number,name,surname,phone_num,age)
               VALUES(?,?,?,?,?)

''',(num,name,surname,phone,age))
db.commit()
