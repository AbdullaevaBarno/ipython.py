import sqlite3


db = sqlite3.connect('studentler.db')

cursor = db.cursor()


# cursor.execute('''
# CREATE TABLE IF NOT EXISTS studentler(
#                ati TEXT,
#                jasi INTEGER,
#                orta_ball REAL
#                )
# ''')
# ati = input('student ati:')
# jasi = int(input('Student jasi:'))
# orta_ball = int(input('studenttin ortasha bali:'))
# cursor.execute('''
# INSERT INTO studentler(ati,jasi,orta_ball)
#                 VALUES(?,?,?)
# ''',(ati,jasi,orta_ball))

# cursor.execute('''
# UPDATE studentler
#                SET jasi=21
#                WHERE ati='Anna'
# ''')

# cursor.execute('''
# DELETE FROM studentler
#                WHERE ati='Butrus'
# ''')

# cursor.execute('SELECT * FROM studentler')#select - saylaw

# modeller = cursor.fetchall()
# print(modeller)

# cursor.execute('SELECT jasi>20 FROM studentler')#select - saylaw

# modeller = cursor.fetchall()
# print(modeller)

cursor.execute('''
CREATE TABLE IF NOT EXISTS kitaplar(
               ati TEXT,
               avtori TEXT,
               jili INTEGER
               )
''')
# ati = input('kitaptin ati:')
# avtori = input('kitaptin avtori:')
# jili = int(input('shiqqan jili:'))

# cursor.execute('''
# INSERT INTO kitaplar(ati,avtori,jili)
#                 VALUES(?,?,?)
# ''',(ati,avtori,jili))

# cursor.execute('''SELECT ati FROM kitaplar
#                WHERE ati LIKE 'd%' ''')
# atlar=cursor.fetchall()
# print(atlar)
# atlari = ['Dunyoning ishlari', '1984', 'Urush va Tinchlik', 'Mungli kozlar']

# ati = [ati for ati in atlari if ati.lower().startswith("d")]
# print(ati)

db.commit()