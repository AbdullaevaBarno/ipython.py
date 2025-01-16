# import tkinter
# window = tkinter.Tk()
# window.geometry('1250x700')#ширина x длина
# window.title('Translate language')
# window.configure(background='#22177A')

# from_lbl = tkinter.Label(text='From language',
#                               font=('Calibri',20),
#                               )
# from_lbl.place(x=70,y=100)


# from_lang_lbl=tkinter.Text(font=('Franklin Gothic Medium',15),
#                          background='white',
#                          foreground='#3D3BF3'
#                          )
# from_lang_lbl.place(x=70,y=155,width=500,height=400)

# from_lang_lbl_2=tkinter.Text(font=('Franklin Gothic Medium',30),
#                          background='white',
#                          foreground='#3D3BF3'
#                          )
# from_lang_lbl_2.place(x=650,y=155,height=400,width=520)

# trans_btn = tkinter.Button(text='Translate',
#                               font=('Franklin Gothic Medium',25),
#                               background='white',
#                               foreground='black',
#                               )
# trans_btn.place(x=525,y=585)


# window.mainloop()

import tkinter

import translators
def perevod():
    text = from_lang_text.get(0.0,tkinter.END)
    from_lang = languages[strinvar1.get()]
    to_lang = languages[strinvar2.get()]
    translate = translators.translate_text(
        query_text=text,
        from_language=from_lang,
        to_language=to_lang
    )
    to_lang_text.insert(0.0,translate)

window = tkinter.Tk()
window.title('Translator')
window.geometry('600x750+500+10')
window.configure(background='#81BFDA')
#iconka qoyiw
iconca=tkinter.PhotoImage(file='translate.png')
window.iconphoto(1,iconca)

from_lang_lbl = tkinter.Label(
    text='From Language:',
    font=('Calibri',20),
    background='#81BFDA',
    fg='#0A3981'
)
from_lang_lbl.place(x=20,y=20)
strinvar1 = tkinter.StringVar()
languages = {
    'Russian':'ru',
    'English':'en',
    'Finnish':'fi',
    'Arabic':'ar',
    'Korean':'ko',
    'turkish':'tr',
    'uzbek':'uz',
}
from_lang_menu = tkinter.OptionMenu(
    window,
    strinvar1,*languages,
    
)
from_lang_menu.config(font=('Calibri',20),
                      fg='red')
from_lang_menu.place(x=220,y=20)

from_lang_text = tkinter.Text(
    font=('Calibri',16)
)
from_lang_text.place(x=50,y=80,
                     height=250,
                     width=500)
strinvar2 = tkinter.StringVar()
translate_btn = tkinter.Button(
    text='Translate',
    font=('Calibri',20),
    foreground='white',
    background='#0A5EB0',
    command=perevod)
translate_btn.place(x=250,y=350)
to_lang_lbl = tkinter.Label(
    text='To language:',
    font=('Calibri',20),
    background='#81BFDA',
    fg='#0A3981'
)
to_lang_lbl.place(x=20,y=420)
to_lang_text = tkinter.Text(
    font=('Calibri',16),
    foreground='#0A97B0'
)

to_lang_menu = tkinter.OptionMenu(
    window,
    strinvar2,*languages,
    
)
to_lang_menu.config(font=('Calibri',20),
                    fg='red')
to_lang_menu.place(x=200,y=420)

to_lang_text.place(x=50,y=480,
                   height=250,
                   width=500)
window.mainloop()
