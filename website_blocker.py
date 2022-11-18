#Uruchom Terminal jako administrator przed włączeniem tego cudownego kodu xd
#Zainstaluj tk w terminalu przed włączeniem tego cudownego kodu poprzez wpisanie w terminalu: pip install tk
from tkinter import *

window = Tk()
window.geometry('650x400')
window.minsize(650,400)
window.maxsize(650,400)
window.title("Blokowacz reklam xd")

heading=Label(window, text ='Blokowacz reklam' , font ='arial')
heading.pack()

host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

label1=Label(window, text ='Adres strony :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)

enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)

def Blocker():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                display=Label(window, text = 'Zostało już Zablokowane' , font = 'arial')
                display.place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text = "Zablokowane", font = 'arial').place(x=230,y =200)

def Unblock():
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.readlines()
    for web in Website:
            if web in website_lists:
                with open (host_path , 'r+') as f:
                    for line in file_content:
                        if line.strip(',') != website_lists:
                            f.write(line)
                            Label(window, text = "Odblokuj", font = 'arial').place(x=350,y =200)
                            pass
                        else:
                            display=Label(window, text = 'Zostało już odblokowane' , font = 'arial')
                            display.place(x=350,y=200)


block_button = Button(window, text = 'Zablokuj',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'royal blue1', activebackground = 'grey')
block_button.place(x = 230, y = 150)

unblock_button = Button(window, text = 'Odblokuj',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'royal blue1', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)
window.mainloop()
