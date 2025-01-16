#GUI- Grafic User Interfeys

import tkinter
window = tkinter.Tk()
window.geometry('600x500')#ширина x длина
window.title('My first programm')
window.configure(background='#0A3981')

label1=tkinter.Label(text='Menin birinshi programmam',
                     font=('Arial Rounded MT Bold',20),
                     background='#0A3981',
                     foreground='#80C4E9'
                     )
label1.pack()

entry2=tkinter.Entry(font=('Arial Rounded MT Bold',20))
entry2.pack()

button1=tkinter.Button(text='Нажимай',
                       font=('Arial Rounded MT Bold',20),
                       background='#80C4E9',
                       foreground='black',
                       
)
button1.pack()

entry1=tkinter.Entry(font=('Arial Rounded MT Bold',20))
entry1.pack()

button2=tkinter.Button(text='Очистить',
        font=('Arial Rounded MT Bold',20),
        background='red',
        foreground='black'
)
button2.pack()
window.mainloop()