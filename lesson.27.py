#GUI- Grafic User Interfeys

import tkinter
window = tkinter.Tk()
window.geometry('600x500')#ширина x длина
window.title('My first programm')
window.configure(background='#001F3F')

label1=tkinter.Label(text='Моя первая прогамма',
                    font =('Impact',25),
                     background='#001F3F',
                     foreground='#80C4E9'
                     )
label1.pack()

entry2=tkinter.Entry(font=('Arial Rounded MT Bold',30),
                     background='#80C4E9')
entry2.pack(pady=10)

button1=tkinter.Button(text='Нажимай',
                       font=('Impact',20),
                       background='#80C4E9',
                       foreground='black',
                       
)
button1.pack(padx=10,pady=10)

entry1=tkinter.Entry(font=('Arial Rounded MT Bold',30),
                     background='#80C4E9')
entry1.pack()

button2=tkinter.Button(text='Очистить',
        font=('Impact',20),
        background='red',
        foreground='black'
)
button2.pack(pady=10)
window.mainloop()