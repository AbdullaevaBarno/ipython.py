# import tkinter
# window = tkinter.Tk()
# window.geometry('900x600')#ширина x длина
# window.title('My first programm')
# window.configure(background='#78B3CE')
# window.title('Salary Calculator')
# #iconka qoyiw
# iconca=tkinter.PhotoImage(file='quality.png')
# window.iconphoto(1,iconca)
# label1=tkinter.Label(text='SALARY :',
#                      font=('ALGERIAN',30),
#                      background='#78B3CE',
#                      foreground='White'
#                      )
# label1.place(x=0,y=30)

# entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20),
#                      background='#4CC9FE')
# entry2.place(x=200,y=35)

# button1=tkinter.Button(text='CALCULATE',
#                        font=('ALGERIAN',23),
#                        background='#4CC9FE',
#                        foreground='White',
                       
# )
# button1.place(x=600,y=60)

# label1=tkinter.Label(text='TAXEC :',
#                      font=('ALGERIAN',30),
#                      background='#78B3CE',
#                      foreground='White'
#                      )
# label1.place(x=0,y=120)

# entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20),
#                      background='#4CC9FE')
# entry2.place(x=200,y=125)

# button1=tkinter.Button(text='CLEAR',
#                        font=('ALGERIAN',23),
#                        background='#4CC9FE',
#                        foreground='White',
                       
# )
# button1.place(x=640,y=155)

# label1=tkinter.Label(text='FOR ME :',
#                      font=('ALGERIAN',30),
#                      background='#78B3CE',
#                      foreground='White'
#                      )
# label1.place(x=0,y=215)

# entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20),
#                      background='#4CC9FE')
# entry2.place(x=200,y=220)

# button1=tkinter.Button(text='QUIT',
#                        font=('ALGERIAN',22),
#                        background='#B8001F',
#                        foreground='White',
                       
# )
# button1.place(x=650,y=260)

# label1=tkinter.Label(text='REMAINS :',
#                      font=('ALGERIAN',30),
#                      background='#78B3CE',
#                      foreground='White'
#                      )
# label1.place(x=0,y=300)


# entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20),
#                      background='#4CC9FE')
# entry2.place(x=200,y=305)
# window.mainloop()

######
import tkinter
window = tkinter.Tk()
window.geometry('1000x900')#ширина x длина
window.title('Registration')
window.configure(background='#7D7C7C')

def send_data():
    name = entry1.get()
    surname = entry2.get()
    login = entry3.get()
    password = entry4.get()
    phone = entry5.get()

    file = open(file='data.txt', mode='a')
    file.write(f"Name: {name}\n")
    file.write(f"Surname: {surname}\n")
    file.write(f"Login: {login}\n")
    file.write(f"Password: {password}\n")
    file.write(f"Phone Number: {phone}\n")

def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    entry5.delete(0,tkinter.END)

def password():
    if entry4['show']=='•':
         entry4['show']=''
    else:
        entry4['show']="•"

def exit():
    from tkinter import messagebox
    msgbox = messagebox.askyesno(message='Confirm the operation?', title='Transaction confirmation')
    if msgbox==True:
           window.exit()
    
label1=tkinter.Label(text='Name:',
                      font=('Franklin Gothic Medium',22),
                      background='#7D7C7C',
                      foreground='black'
                      )
label1.place(x=90,y=70)

entry1=tkinter.Entry(font=('Arial Rounded MT Bold',25),
                      background='white')
entry1.place(x=350,y=69)

label2=tkinter.Label(text='Surname:',
                      font=('Franklin Gothic Medium',22),
                      background='#7D7C7C',
                      foreground='black'
                      )
label2.place(x=90,y=170)

entry2=tkinter.Entry(font=('Arial Rounded MT Bold',25),
                      background='white')
entry2.place(x=350,y=170)

label3=tkinter.Label(text='Login:',
                      font=('Franklin Gothic Medium',22),
                      background='#7D7C7C',
                      foreground='black'
                      )
label3.place(x=90,y=275)

entry3=tkinter.Entry(font=('Arial Rounded MT Bold',25),
                      background='white')
entry3.place(x=350,y=275)

label4=tkinter.Label(text='Password:',
                      font=('Franklin Gothic Medium',22),
                      background='#7D7C7C',
                      foreground='black'
                      )
label4.place(x=90,y=385)

entry4=tkinter.Entry(font=('Arial Rounded MT Bold',25),
                      background='white')
entry4.place(x=350,y=385)

password_btn = tkinter.Button(
     text='glass.png',
     background='white',
     font=('Franklin Gothic Medium',22),
     border=0,
     command=password
)
password_btn.place(x=730,y=385,
                   height=42
)
label5=tkinter.Label(text='Phone Number:',
                      font=('Franklin Gothic Medium',22),
                      background='#7D7C7C',
                      foreground='black'
                      )
label5.place(x=90,y=490)

entry5=tkinter.Entry(font=('Arial Rounded MT Bold',25),
                      background='white')
entry5.place(x=350,y=490)

button1=tkinter.Button(text='Send',
                       font=('Bahnschrift Semilight',28),
                       background='white',
                       foreground='black',
                       command=send_data
                       
)
button1.place(x=200,y=590)

button2=tkinter.Button(text='Clear',
                       font=('Bahnschrift Semilight',28),
                       background='white',
                       foreground='black',
                       command=clear
                       
)
button2.place(x=650,y=590)

button3=tkinter.Button(text='Exit',
                       font=('Bahnschrift Semilight',28),
                       background='white',
                       foreground='black',
                       command=exit
                       
)
button3.place(x=440,y=690)

window.mainloop()