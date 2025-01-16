import tkinter
import math
window = tkinter.Tk()
window.geometry('700x700')#ширина x длина
window.title('Triangle')
window.configure(background='#FAB12F')
def peremetr():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    p = a+b+c
    entry4.insert(0,p)

def maydan():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    entry5.insert(0,s)

def info():
    a = int(entry1.get())
    b = int(entry2.get())
    c = int(entry3.get())
    if a==b==c:
        ushmuyeshlik_turi = 'a=b=c'
    elif a==b or a==c or b==c:
        ushmuyeshlik_turi = 'Ten qaptalli'
    else:
        ushmuyeshlik_turi = 'a=!b=!c'
    entry6.insert(0,ushmuyeshlik_turi)

def clear():
    entry1.delete(0,tkinter.END)
    entry2.delete(0,tkinter.END)
    entry3.delete(0,tkinter.END)
    entry4.delete(0,tkinter.END)
    entry5.delete(0,tkinter.END)
    entry6.delete(0,tkinter.END)
label_a=tkinter.Label(text='a',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white'
                      )
label_a.place(x=0,y=30)

entry1=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry1.place(x=35,y=40,width=100)

label_b=tkinter.Label(text='b',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white'
                      )
label_b.place(x=0,y=80)

entry2=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry2.place(x=35,y=90,width=100)

label_c=tkinter.Label(text='c',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white'
                      )
label_c.place(x=0,y=130)

entry3=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry3.place(x=35,y=142,width=100)

label_p=tkinter.Label(text='p',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white',
                      )
label_p.place(x=450,y=30)

entry4=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry4.place(x=490,y=40,width=120)

label_s=tkinter.Label(text='s',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white'
                      )
label_s.place(x=450,y=80)

entry5=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry5.place(x=490,y=90,width=120)

label_in=tkinter.Label(text='info',
                      font=('Franklin Gothic Medium',22),
                      background='#FAB12F',
                      foreground='white'
                      )
label_in.place(x=450,y=130)

entry6=tkinter.Entry(font=('Franklin Gothic Medium',15),
                      background='white')
entry6.place(x=520,y=140,width=130)

button1=tkinter.Button(text='clear',
                        font=('Impact',20),
                        background='#B8001F',
                        foreground='black',
                        command=clear
)
button1.place(x=170,y=190)

button2=tkinter.Button(text='result',
                        font=('Impact',20),
                        background='#6EC207',
                        foreground='black',
                        command=peremetr
                       
)
button2.place(x=280,y=190)

button3=tkinter.Button(text='area',
                        font=('Impact',20),
                        background='#6EC207',
                        foreground='black',
                        command=maydan
                       
)
button3.place(x=390,y=190)

button2=tkinter.Button(text='info',
                        font=('Impact',20),
                        background='#6EC207',
                        foreground='black',
                        command=info
                       
)
button2.place(x=490,y=190)

window.mainloop()