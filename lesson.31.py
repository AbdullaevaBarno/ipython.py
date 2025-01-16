import tkinter
window = tkinter.Tk()
window.geometry('1000x900')#ширина x длина
window.title('QRCode Generator')
window.configure(background='#22177A')
window.option_add("*tearOff", False)
from tkinter import messagebox
def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")

main_menu = tkinter.Menu()
file_menu = tkinter.Menu(tearoff=0)
settings_menu = tkinter.Menu()
 
settings_menu.add_command(label="Save")
settings_menu.add_command(label="Open")
 
file_menu.add_cascade(label="Settings", menu=settings_menu) 
file_menu.add_separator()
file_menu.add_command(label="Exit")
file_menu.add_command(label="New")
file_menu.add_command(label="Save")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit,background='red')
 
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit",command=edit_click)
main_menu.add_cascade(label="View")
 
main_menu.add_cascade(label="File", menu=file_menu)
 
window.config(menu=main_menu)

def clear():
    entry_poe.delete(0,tkinter.END)

def quit():
    from tkinter import messagebox
    msg = messagebox.askyesno(title='Example',
                              message='Shigiwdi qaleysizbe?')
    if msg==True:
        window.quit()

def generate():
    import qrcode
    url = entry_poe.get()
    img = qrcode.make(url)
    img.save("some_file.png")
    photo = tkinter.PhotoImage(file="some_file.png")
    lbl_for_qrcode = tkinter.Label(
        image=photo
    )
    lbl_for_qrcode.image=photo
    lbl_for_qrcode.place(x=400,y=250)

QRC_label=tkinter.Label(text='QRCode Generator',
                     font=('Franklin Gothic Medium',25),
                     background='#22177A',
                     foreground='#3D3BF3'
                     )
QRC_label.pack(pady=20)

URL_label=tkinter.Label(text='URL :',
                     font=('Franklin Gothic Medium',20),
                    background='#22177A',
                     foreground='#3D3BF3'
                     )
URL_label.place(x=0,y=150)

entry_poe=tkinter.Entry(font=('Franklin Gothic Medium',40),
                         background='#22177A',
                         foreground='#3D3BF3'
                         )
entry_poe.place(x=70,y=155,height=30)

generate_btn = tkinter.Button(text='Generate',
                              font=('Franklin Gothic Medium',20),
                              background='#3D3BF3',
                              foreground='black',
                              command=generate
                              )
generate_btn.place(x=70,y=220,width=140,height=50)

clear_btn = tkinter.Button(text='Clear',
                              font=('Franklin Gothic Medium',20),
                              background='#3D3BF3',
                              foreground='black',
                              command=clear
                              )
clear_btn.place(x=70,y=290,width=140,height=50)

quit_btn = tkinter.Button(text='Quit',
                              font=('Franklin Gothic Medium',20),
                              background='#3D3BF3',
                              foreground='black',
                              command=quit
                              )
quit_btn.place(x=70,y=360,width=140,height=50)

window.mainloop()