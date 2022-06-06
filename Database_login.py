import pandas as pd
from tkinter import *
from tkinter import ttk
import random, string

screen = Tk()
screen.geometry('300x250')
screen.title('Stasiun SoJoPurBaja')
Label(text = 'Stasiun SoJoPurBaja', bg= 'grey', font= ('times new roman', 13)).pack()

def login():
    userData = pd.read_csv('DatabaseAkun.csv')
    df = pd.DataFrame(userData)

    global Username
    global Password
    
    e1=Entry(screen)
    e1.grid(row=0,column=1)
    e2=Entry(screen)
    e2.grid(row=1,column=1)

    Username= e1.get()
    Password=e2.get()
 
    matching_creds = (len(df[(df.username == Username) & (df.password == Password)]) > 0)

    if matching_creds:
        print('success')
    else:
        print('\nYour account is not registered yet!')
        print('please contact admin')

def register():
    userData = pd.read_csv('DatabaseAkun.csv')
    df = pd.DataFrame(userData)
    
    global Username
    global Password

    e1=Entry(screen)
    e1.grid(row=0,column=1)
    e2=Entry(screen)
    e2.grid(row=1,column=1)
    e3=Entry(screen)
    e3.grid(row=2,column=1)
    e4=Entry(screen)
    e4.grid(row=3,column=1)
    e5=Entry(screen)
    e5.grid(row=4,column=1)
    e6=Entry(screen)
    e6.grid(row=5,column=1)
    e7=Entry(screen)
    e7.grid(row=6,column=1)
    e8=Entry(screen)
    e8.grid(row=7,column=1)

    mylabel1 = Label(screen, text='Username')
    mylabel1.grid(row=0,column=0)
    mylabel2 = Label(screen, text='Password')
    mylabel2.grid(row=1,column=0)
    mylabel3 = Label(screen, text='Nama Lengkap')
    mylabel3.grid(row=2,column=0)
    mylabel4 = Label(screen, text='Nomor KTP')
    mylabel4.grid(row=3,column=0)
    mylabel5 = Label(screen, text='Email')
    mylabel5.grid(row=4,column=0)
    mylabel6 = Label(screen, text='Nomor Telepon')
    mylabel6.grid(row=5,column=0)
    mylabel7 = Label(screen, text='Tanggal Lahir')
    mylabel7.grid(row=6,column=0)
    mylabel8 = Label(screen, text='Jenis Kelamin')
    mylabel8.grid(row=7,column=0)

    Username = e1.get()
    Password= e2.get()
    Nama_Lengkap= e3.get()
    Nomor_KTP = e4.get()
    Email = e5.get()
    No_Telp = e6.get()
    Tanggal_Lahir = e7.get()
    Jenis_Kelamin = e8.get()


    matching_creds = (len(df[(df.Username == Username) ]) < 1 or len(df[(df.Password == Password) ]) < 1)

    if matching_creds and Username != "":
        print('success')
        newuser = {'Username' : [Username],
                'Password' : [Password],
                'NamaLengkap' : [Nama_Lengkap],
                'NomorKTP' : [Nomor_KTP],
                'Email' : [Email],
                'NomorTelpon' : [No_Telp],
                'TanggalLahir' : [Tanggal_Lahir],
                'JenisKelamin' : [Jenis_Kelamin],}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('DatabaseAkun', mode='a', index=False, header=False)
    else:
        print('Username or number already exist')
screen.mainloop