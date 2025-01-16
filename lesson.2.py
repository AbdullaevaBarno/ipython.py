#1
#my_list1=['kurtka', 'palto', 'krassovka']
#my_list2=['sportivka', 'djempir', 'shlyapa']
#tovarlar={"satip alingan": my_list1,
#          "satip aliniw kerek": my_list2}
#soraw=input("sizge kerek?: (salip alingan/satip aliniwi kere):")
#if soraw.lower()=="satip alingan":
#    print("satip alingan")
#2
#my_list=[1,2,3,4]
#my_dict={1:1,
#         2:2,
#         3:3,
#         4:4}
#print(my_dict)
#3
#num='111222000355222244'
#dict={0:3, 1:3, 2:7, 3:1, 4:2, 5:2}
#print(dict)
#4
#haripler={"A":1, "E":1, "I":1, "O":1, "U":1, "L":1, "N":1, "S":1, "T":1, "R":1, "D":2, "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "J":8}
#soz=soz.upper()
#uliwma_haripler=0
#for 
#5
#6

#homework_dict
#1
#my_dict={}
#my_dict["apple"]=5
#my_dict["banana"]=3
#my_dict["orange"]=7
#print(my_dict)
#2
#my_dict["banana"]=6
#print(my_dict)
#3
#for gilt,qiymat in my_dict.items():
# print("gilt:",  gilt)
#4
#for qiymat in my_dict.values():
# print(f"qiymat: {qiymat}")
#5
#for gilt in my_dict.keys():
# print(f"Gilt: {gilt} ")
#6#
#my_dict.pop('orange')
#print(my_dict)
#7
#my_dict["juzim"]=6
#print(my_dict)
#8
#my_dict={"apple": 5,
#         "banana": 6,
#         "juzim": 6}
#for gilt, qiymat in my_dict.items():
# print(f' gilt: {gilt}, qiymat: {qiymat}')
#9
#generatori
#squard_dict={i: i**2 for i in range(1,6)}
#print(squard_dict)
#10
#iteratot=iter(squard_dict.items())
#for gilt, qiymat in iteratot:
# print(f'gilt: {gilt}, qiymat: {qiymat}')
#11
#filtered_dict={gilt: qiymat for gilt, qiymat in my_dict.items() if qiymat>4}
#print(filtered_dict)
#12
#my_dict2={"kiwi": 7,
#          "orange": 8}
#my_dict.update(my_dict2)
#print(my_dict)
#13
#kobeytiw= {gilt: qiymat*2 for gilt, qiymat in my_dict.items()}
#print(kobeytiw)
#14#
#grouped_dict={}
#for gilt, qiymat in my_dict.items():
# grouped_dict.setdefault(qiymat,[]).append(gilt)
#print(grouped_dict)
#15
#if 'apple' in my_dict:
# print('"Apple" gilti lugatda bar')
#else:
# print('"Aplle" gilti lugatda joq')