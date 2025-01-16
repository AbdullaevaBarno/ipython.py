#dict

#list , tuple, set

# my_dict = {}

# print(type(my_dict))

# my_dict2 = dict()
# print(type(my_dict2))


# sozlik = {'apple':'alma',
#           'book':'kitap',
#           'pen':'qalem',
#           'pencil':'ruchka',
#           'people':'adam',
#           'key':'value'}

# print(sozlik)
# print(sozlik['key'])



# contacts = {
#     'Janibek':'+998999999999',
#     'Abdullax':'+998977777777',
#     'Azamat':'+998900000000',
#     'Muxammed':'+1253657845374',
# }

# print(contacts['Janibek'])


# contacts['Muxammed']='+998988888888'#usinday qilip ozgertemiz
# print(contacts)

# contacts['Arman']='+998911111111'#element qosiw
# print(contacts)


# contacts['Abdullax']='+998933030303'
# print(contacts)

# print(contacts)
# contacts.pop('Muxammed')
# print(contacts)

#my_dict={'Xurshida':'Abibullaeva',
#        'Muxammed': 'Sarsenbaev',
#        'Umida':'Zayorova',
#        'Aziza':'Torebaeva',
#       'Dildora':'Yawmutbaeva'
#}
#print(my_dict)
#print(my_dict['Dildora'])
#my_dict.pop('Muxammed')
#print(my_dict)

#1
#my_dict={'apple':'alma',
#         'banana':'banan', 
#         'cherry':'shiye'}
#my_dict.pop('banana')
#print(my_dict) 

#2
#dict1={'apple':'alma',
#       'kiwi':'kivi',
#       'pineapple':'almurt',
#}
#dict2={'banana':'banan',
#       'orange':'opelsin',
#       'icecream':'morojniy'}
#dict1.update(dict2)
#print(dict1)

#3
#my_dict.pop()
#print(my_dict)

#4
#my_dict={"a": 1,
#         "b": 2,
#         "c": 3
#}
#new_key=input('Giltti kirgizin:')
#new_value=input('Qiymatti kirgizin:')
#my_dict.update({new_key: new_value})
#print(my_dict)

#5#
#my_list=[1,2,2,4,6,7,8,8]
#count_dict={}
#for element in my_list:
#    if element not in count_dict:
#        count_dict.update({element:1})
#    else:
#        count_dict[element]=count_dict[element]+1
#n_count=0
#for key in list(count_dict.keys()):
#    if count_dict[key]==1:
#        n_count=n_count+1
#    count_dict.pop(key)
#print(n_count)

#6
#my_dict={"a": 10,
#         "b": 20,
#         "c": 30}
#value=my_dict.pop("b")
#print(value)
#print(my_dict)

#7#
#gilt=input('gilt:')
#qiymat=input('qiymat:')
#if gilt in my_dict:
#    eski_qiymat=my_dict.pop(gilt)
##    print(f"eski qiymat: '{gilt}'{eski_qiymat} oshirildi")
#    my_dict.update({gilt: qiymat})
#    print(f"dict janalandi:{gilt} -> {qiymat}")
#else:
#    print(f"Gilt {gilt} dictte tabilmadi")
#print(f"janalangan dict: {my_dict}")        

#8
#dict1={"a": 10,
#       "b": 20,
#       "c": 30,
#       "d": 40}
#dict2={"b": 2,
#       "c": 3,
#       "e": 5}
#for gilt in dict2.keys():
#    if gilt in dict1:
#       dict2.update({gilt: dict1[gilt]})
#print(dict2)

#9
# Berilgen lug'at
#my_dict = {"a": 10, "b": 20, "c": 30}

# Paydalaniwshidan gilt kiritiwin soraymiz
#gilt = input("Oshirejaq bolgan giltti kiritin: ")

# Giltti tekseremiz ham oshiremiz
#qiymat = my_dict.pop(gilt, None)
#if qiymat is not None:
#    print(f"'{gilt}' gilti oshirildi, onin qiymati: {qiymat}")
#else:
#    print(f"Xato: '{kalit}' gilti lug'atda tabilmadi.")
#print("Janalangan lug'at:", my_dict)

#10
# Berilgen lug'at
#my_dict = {"a": 5, "b": 15}

# Paydalaniwshidan san kiritiwin soraymiz
#x = int(input("Son kiriting: "))

# Shart arqali lug'atti janalaw
#if x >= 10:
#    my_dict.update({"new_key": x})
#print("Janalangan lug'at:", my_dict)

#11
#Lug'at (dict) — bu Python'dagi kalit-qiymat juftliklari asosida tashkil etilgan ma'lumotlar tuzilmasi.
#Lug'atda har bir elementga kalit orqali murojaat qilinadi, indeks orqali emas.
#Kalitlar o'zgarmas (immutable) bo'lishi kerak (masalan, string, tuple, integer).
#Lug'atlar tartiblanmagan va o'zgartiriladigan (mutable) tuzilma hisoblanadi.

#12
#lugat.pop(gilt, [standart_qiymat])
#kalit — o'chiriladigan kalit nomi.
#Agar kalit mavjud bo'lmasa, standart_qiymat qaytariladi. Aks holda, KeyError xatosi yuzaga keladi.

#13
#Agar pop() chaqirilganda kalit mavjud bo'lmasa va standart qiymat ko'rsatilmagan bo'lsa, KeyError xatosi yuzaga keladi.

#14
#my_dict = {"a": 10, "b": 20}
#qiymat = my_dict.pop("a")
#print(qiymat)  # Natije: 10
#print(my_dict)  # Natije: {'b': 20}

#15
#dict1 = {"a": 10}
#dict2 = {"b": 20}
#dict1.update(dict2)
#print(dict1)

#16
#Ha, mumkin. update() yordamida yangi kalit-qiymat juftliklarini lug'atga qo'shish mumkin.

#17
#Agar update() ga noto'g'ri turdagi argument berilsa, TypeError xatosi yuzaga keladi.

#18
#dict1 = {"a": 1, "b": 2}
#dict2 = {"c": 3}
#dict1.update(dict2)
#print(dict1)

#19
#Element qo'shish: lugat[kalit] = qiymat
#Element o'chirish: del lugat[kalit]
#Barcha elementlarni o'chirish: lugat.clear()

#20
#Tayinlash operatori (=):
#Faqat bitta kalit-qiymat juftligini qo'shish yoki o'zgartirish uchun ishlatiladi.
#lugat["yangi_kalit"] = 100
#update() usuli:
#Bir nechta kalit-qiymat juftliklarini bir vaqtning o'zida yangilash yoki qo'shish uchun ishlatiladi.
#lugat.update({"a": 1, "b": 2})


#homework
#1
my_dict={}
#print(my_dict)

#2
my_dict["ati"]="Jon"
#print(my_dict)

#3
my_dict["jasi"]=25
#print(my_dict)

#4
print("jasi:", my_dict["jasi"])

#5
my_dict["jasi"]=26
#print(my_dict)

#6
#if "gender" not in my_dict:
#    my_dict["gender"]="erkek"
#print(my_dict)

#7
another_dict={"kasip":"programmist",
              "milleti": "ozbek"}
my_dict.update(another_dict)
#print(my_dict)

#8
#my_dict.pop("gender")
#print(my_dict)

#9
#if "ati" in my_dict:
#    my_dict.pop("ati")
#print(my_dict)

#10
#for gilt in my_dict.keys():
#    print("gilt:", gilt)

#11
#for qiymat in my_dict.values():
#    print("qiymat:", qiymat)

#12
#for gilt, qiymat in my_dict.items():
#    print(f"{gilt}: {qiymat}")

#13
#gilt_list=list(my_dict.keys())
#print(gilt_list)

#14
#qiymat_list=list(my_dict.values())
#print(qiymat_list)

#15
#print(len(my_dict))

#16
#city=my_dict.get("city", "tabilmadi")
#print("mamleket:", city)

#17
#print("Giltler:", my_dict.keys())

#18
#print("Qiymatlar:", my_dict.values())

#19
#copy_dict= my_dict.copy()
#print("Kopiya:", copy_dict)

#20
#my_dict.clear()
#print("Tazalangan lu'gat:", my_dict)