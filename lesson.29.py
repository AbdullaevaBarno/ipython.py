# import tkinter
# window = tkinter.Tk()
# window.geometry('600x500')#ширина x длина
# window.title('My first programm')
# window.configure(background='#001F3F')
# def example():
#     #print(entry2.get(entry1))
#     #insert(index,element)
#     #entry1.insert(0,'Zinur')#get - aliw, insert -qosiw(saliw),delete - oshiriw
#     #entry2.delete(0,tkinter.END)
#     info = entry2.get() #aliw
#     entry1.insert(0,info)
# def delete():
#     entry1.delete(0,tkinter.END)
#     entry2.delete(0,tkinter.END)
# label1=tkinter.Label(text='Моя первая прогамма',
#                      font=('Impact',25),
#                      background='#001F3F',
#                      foreground='#80C4E9'
#                      )
# label1.pack()

# entry2=tkinter.Entry(font=('Arial Rounded MT Bold',30),
#                      background='#80C4E9')
# entry2.pack(pady=10)

# button1=tkinter.Button(text='Нажимай',
#                        font=('Impact',20),
#                        background='#80C4E9',
#                        foreground='black',
#                        command=example
                       
# )
# button1.pack(padx=10,pady=10)

# entry1=tkinter.Entry(font=('Arial Rounded MT Bold',30),
#                      background='#80C4E9')
# entry1.pack()

# button2=tkinter.Button(text='Очистить',
#         font=('Impact',20),
#         background='red',
#         foreground='black',
#         command=delete
# )
# button2.pack(pady=10)
# window.mainloop()


import tkinter
window = tkinter.Tk()
window.geometry('900x600')#ширина x длина
window.title('My first programm')
window.configure(background='#78B3CE')
window.title('Salary Calculator')
#iconka qoyiw
iconca=tkinter.PhotoImage(file='quality.png')
window.iconphoto(1,iconca)

def calc():
    salary = int(entry1.get())
    taxes = int(entry2.get())
    for_me = int(entry3.get())
    remains = salary-taxes-for_me
    entry4.insert(0,remains)
def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
def quit():
    from tkinter import messagebox
    msgbox = messagebox.askyesno(message='Confirm the operation?', title='Transaction confirmation')
    if msgbox==True:
           window.quit()
label1=tkinter.Label(text='SALARY :',
                      font=('ALGERIAN',30),
                      background='#78B3CE',
                      foreground='White'
                      )
label1.place(x=0,y=30)

entry1=tkinter.Entry(font=('Arial Rounded MT Bold',20),
                      background='#4CC9FE')
entry1.place(x=200,y=35)

button1=tkinter.Button(text='CALCULATE',
                        font=('ALGERIAN',23),
                        background='#4CC9FE',
                        foreground='White',
                        command=calc
                       
)
button1.place(x=600,y=60)

label1=tkinter.Label(text='TAXEC :',
                      font=('ALGERIAN',30),
                      background='#78B3CE',
                      foreground='White'
                      )
label1.place(x=0,y=120)

entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20),
                      background='#4CC9FE')
entry2.place(x=200,y=125)

button1=tkinter.Button(text='CLEAR',
                        font=('ALGERIAN',23),
                        background='#4CC9FE',
                        foreground='White',
                        command=clear
                       
)
button1.place(x=640,y=155)

label1=tkinter.Label(text='FOR ME :',
                      font=('ALGERIAN',30),
                      background='#78B3CE',
                      foreground='White'
                      )
label1.place(x=0,y=215)

entry3=tkinter.Entry(font=('Arial Rounded MT Bold',20),
                      background='#4CC9FE')
entry3.place(x=200,y=220)

button1=tkinter.Button(text='QUIT',
                        font=('ALGERIAN',22),
                        background='#B8001F',
                        foreground='White',
                        command=quit
                       
)
button1.place(x=650,y=260)

label1=tkinter.Label(text='REMAINS :',
                      font=('ALGERIAN',30),
                      background='#78B3CE',
                      foreground='White',
                      )
label1.place(x=0,y=300)


entry4=tkinter.Entry(font=('Arial Rounded MT Bold',20),
                      background='#4CC9FE')
entry4.place(x=200,y=305)
window.mainloop()