#exam3

#1
#iterator
#dizim=[]
#for i in range(10):
#    dizim.append(i)
#print(dizim) 

#generator
#dizim=[i for i in range(10)]
#print(dizim)

#2
# def uzin_soz(x):
#     return max(x, key=len)
# x = ['Dildora', 'Yulduz', 'Jamshid', 'Roza']
# print(uzin_soz(x))

#3
#list
#Elementler takrarlanadi
#[a,b,c]

#tuple
#Elementlerdi ozgertire almaymiz
#(a,b,c)

#set
#tartipsiz lementler
#{a,b,c}

#4
# import tkinter
# import math
# window = tkinter.Tk()
# window.geometry('700x700')#ширина x длина
# window.title('Window')
# window.configure(background='#FAB12F')
# window.mainloop()

#5
# import tkinter
# window = tkinter.Tk()
# window.geometry('600x500')#ширина x длина
# window.title('My first programm')
# window.configure(background='#001F3F')

# def kosh():
#     text = entry1.get()
#     label.config(text=text)
#     entry1.delete(0,tkinter.END)
# entry1=tkinter.Entry(font=('Arial Rounded MT Bold',30),
#                       background='#80C4E9')
# entry1.pack(pady=10)

# button1=tkinter.Button(text='delete,copy',
#                         font=('Impact',20),
#                         background='#80C4E9',
#                         foreground='black',
#                         command=kosh
# )
# button1.pack(padx=10,pady=10)
# label=tkinter.Label(text="",
#                     font =('Impact',40))
# label.pack()
# window.mainloop()

#6
# import tkinter
# window = tkinter.Tk()
# window.geometry('600x500')#ширина x длина
# window.title('Exam')
# window.configure(background='#001F3F')

# label = tkinter.Label(text='Bugin songi imtihan')
# label.pack()
# window.mainloop()

#7
# def jup_sanlar(start,stop):
#     return [x**2 for x in 
#     range(start, stop + 1) if x%2==0]
# print(jup_sanlar(1,20))

#8
# file=open(file='text.txt', mode='w')
# file.write('Dildora')
# file.close()

#9
# file=open(file='text.txt', mode='r')
# copied=file.read()
# file=open(file='example.txt', mode='w')
# file.write(copied)
#10
# a=int(input('birinshi:'))
# b=int(input('ekinshi:'))
# c=int(input('ushinshi:'))
# kishi = min(a,b,c)
# print(kishi)

#11
# def ulken_h(text):
#     return text.upper()
# print(ulken_h("barno"))

#12
# def sort_text(text):
#     return sorted(set(text))
# print(sort_text("ananas"))

#13
# def sanlar(start,stop):
#     for i in range(start,stop+1):
#         print(i)
# sanlar(1,20)

#14
# def elementler(*x):
#     return x
# print(elementler(1, 3, 'word'))

#15
# def palindrom(text):
#      text=str(text).lower()
#      return text==text[::1]
# print(palindrom(121))


#16
#upper-hamme haripti ulken qilip beredi
#lower-hamme haripti kishi qilip beredi
#swapcase-hariplerdi terisine qiladi, ulken bolsa kishi, kishi bolsa ulken

#17
#while shart islenemen degenshi takrarlanadi
#for berilgen araliqta isleydi
#while
# i=0
# while i<4:
#     print(i)
#     i=i+1
#for
#for i in range(4):
#    print(i)

#18
#and-bul eki sharttide esapqa algan halda
#or-bul eki sharttin birewin yamasa ekinshisin esapqa algan halda
#in-elementler bar ekenligin tekseredi
#is-birdey ekenligin tekseredi
#not-bul sharttin kerisi
#if-ol shart operatori, tek tuwri shartler ushin
#else-if sharti islemese, isleydi
#elif-qosimsha shartler ushin

#19
# import tkinter
# window = tkinter.Tk()
# window.geometry('600x500')#ширина x длина
# window.title('Window')
# window.configure(background='black')

# label1=tkinter.Label(text='Hello world',
#                      font=('Impact',25),
#                      background='black',
#                      foreground='white'
#                      )
# label1.pack()
# window.mainloop()

#20
# import random
# sanlar = [random.randint(1,30)
# for _ in range(5)]
# print(sum(sanlar))