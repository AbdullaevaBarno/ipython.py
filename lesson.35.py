import sqlite3


db = sqlite3.connect('phones.db')

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS automobiles(
               color TEXT,
               model TEXT,
               brandname TEXT,
               price INTEGER,
               data INTEGER
               )
''')

# model = input('mashina modelin jaz:')
# color = input('Mashina renin jaz:')
# brand = input('mashina brandin jaz:')
# cena = int(input('Mashina cenasin jaz:'))
# data = int(input('mashina jilin  jaz:'))

# cursor.execute('''
# INSERT INTO automobiles(color,model,brandname,price,data)
#                VALUES(?,?,?,?,?)
# ''',(color,model,brand,cena,data))
# db.commit()

#bazadan shigaramiz

# cursor.execute('SELECT * FROM automobiles')#select - saylaw

# modeller = cursor.fetchall()
# print(modeller)

#cursor.execute('''
#UPDATE automobiles
#                SET price=20000
#                WHERE model='Malibu 2'

# ''')
# db.commit()

#cursor.execute('''
#DELETE FROM automobiles
#                WHERE data=0
# ''')

# db.commit()

#tablicani jondew
# cursor.execute('''
# UPDATE automobiles
#                 SET color='black'
#                 WHERE brandname='Mercedes Benz'
# ''')

# cursor.execute('''
# DELETE FROM automobiles
#                 WHERE data=321
# ''')
# cursor.execute('''
# UPDATE automobiles
#                 SET price=90000
#                 WHERE model='Mercedes AMG mp3'
# ''')

# cursor.execute('''
# UPDATE automobiles
#                 SET data=2023
#                 WHERE brandname='Chevrolet'
# ''')

cursor.execute('''
UPDATE automobiles
                SET data=2022
                WHERE color='grey'
''')
db.commit()