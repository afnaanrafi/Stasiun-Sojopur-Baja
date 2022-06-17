from fpdf import FPDF
import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkinter import END
from tkinter.messagebox import askyesno
import os

screen = Tk()
screen.geometry('360x540')
screen.configure(background='white')

#Tampilan Login  & Register
def login():
    global screen1,df
    screen1=Toplevel(screen)
    screen1.geometry('360x540')
    screen1.configure(background='white')
    userData = pd.read_csv('DatabaseAkun.csv')
    df = pd.DataFrame(userData)

    global euser,epass,mylabel1,mylabel2,bt_kembali1,bt_kembali2
    
    mybutton1.pack_forget()
    mybutton2.pack_forget()
    mylabel1.pack_forget()

    mylabel1 = Label(screen1, text='Username', bg = '#296d98',fg = 'white')
    mylabel1.pack()
    euser=Entry(screen1, bg= "grey")
    euser.pack()
    mylabel2 = Label(screen1, text='Password', bg = '#296d98',fg = 'white' )
    mylabel2.pack()
    epass=Entry(screen1, bg= "grey")
    epass.pack()
    

    bt_kembali1 = Button(screen1, 
                  text='Login',
                  borderwidth=2,
                  command= complete_login,
                  bg = 'grey',
                  fg = 'black'  )
    bt_kembali1.pack(side=RIGHT,)
    bt_kembali2 = Button(screen1, 
                  text='Back',
                  borderwidth=2,
                  command= back,
                  bg = 'grey',
                  fg = 'black'  )
    bt_kembali2.pack(side=RIGHT)    


def register():
    mybutton1.pack_forget()
    mybutton2.pack_forget()
    mylabel1.pack_forget()

    userData = pd.read_csv('DatabaseAkun.csv')
    df= pd.DataFrame(userData)

    global e1,e2,e3,e4,e4,e5,e6,e7,e8,mylabela,mylabelb,mylabelc,mylabeld,mylabele,mylabelf,mylabelg,mylabelh,bt_kembali1,bt_kembali2
    mylabela = Label(screen, text='Username')
    mylabela.pack()
    e1=Entry(screen)
    e1.pack()
    mylabelb = Label(screen, text='Password')
    mylabelb.pack()
    e2=Entry(screen)
    e2.pack()
    mylabelc = Label(screen, text='Nama Lengkap')
    mylabelc.pack()
    e3=Entry(screen)
    e3.pack()
    mylabeld = Label(screen, text='Nomor KTP')
    mylabeld.pack()
    e4=Entry(screen)
    e4.pack()
    mylabele = Label(screen, text='Email')
    mylabele.pack() 
    e5=Entry(screen)
    e5.pack()
    mylabelf = Label(screen, text='Nomor Telepon')
    mylabelf.pack()
    e6=Entry(screen)
    e6.pack()
    mylabelg = Label(screen, text='Tanggal Lahir')
    mylabelg.pack()
    e7=Entry(screen)
    e7.pack()
    mylabelh = Label(screen, text='Jenis Kelamin')
    mylabelh.pack()
    pilihane8= ["Laki-Laki", "Perempuan"]
    e8=ttk.Combobox(screen,values=pilihane8,state="readonly")
    e8.pack()


    bt_kembali1 = Button(screen, 
                  text='Register',
                  borderwidth=2,
                  command= complete_register,
                  bg = '#296d98',
                  fg = 'white')
    bt_kembali1.pack()
    
    bt_kembali2 = Button(screen, 
                  text='Back',
                  borderwidth=2,
                  command= clearscreen1,
                  bg = '#296d98',
                  fg = 'white'  )
    bt_kembali2.pack()

def complete_register():
    global Username,Password,Nama_Lengkap,Nomor_KTP,Email,No_Telp,Tanggal_Lahir,jenis_kelamin
    Username = e1.get()
    Password= e2.get()
    userData = pd.read_csv('DatabaseAkun.csv')
    df= pd.DataFrame(userData)
    matching_creds = (len(df[(df.Username == Username) & (df.Password == Password)]) < 1)
    if matching_creds and Username != "":
        message1()
        Nama_Lengkap= e3.get()
        Nomor_KTP = e4.get()
        Email = e5.get()
        No_Telp = e6.get()
        Tanggal_Lahir = e7.get()
        jenis_kelamin = e8.get()
        newuser = {'Username' : [Username],
                'Password' : [Password],
                'NamaLengkap' : [Nama_Lengkap],
                'NomorKTP' : [Nomor_KTP],
                'Email' : [Email],
                'NomorTelpon' : [No_Telp],
                'TanggalLahir' : [Tanggal_Lahir],
                'JenisKelamin' : [jenis_kelamin]}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('DatabaseAkun.csv', mode='a', index=False, header=False)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
    else:
        message4()


def complete_login():
    global userData,Username,Password
    Username = euser.get()
    Password= epass.get()
    userData = pd.read_csv('DatabaseAkun.csv')
    df= pd.DataFrame(userData)
    matching_creds = (len(df[(df.Username == Username) & (df.Password == Password)]) > 0)
    if matching_creds:
        message2()
    else:
        message3()
    

def back():
    screen1.destroy()
    firstscreen()

def bck():
    kursiavailable.pack_forget()
    kursiavb_btn.pack_forget()
    bck_btn.pack_forget()
    pilihkeretascreen()

def bck():
    kursiavailable.pack_forget()
    kursiavb_btn.pack_forget()
    bck_btn.pack_forget()
    pilihkeretascreen()

def message1():
    tkinter.messagebox.showinfo("Register", "Selamat Akun Anda Telah Terdaftar")

def message2():
    tkinter.messagebox.showinfo("Login", "Selamat Login Anda Berhasil")
    menujupilihkeretascreen()

def message3():
    tkinter.messagebox.showinfo("Login", "Akun Anda Belum Terdaftar")

def message4():
    tkinter.messagebox.showinfo("Register", "Isi Penuh Isian yang Ada")
def message5():
    answer = askyesno(title='confirmation',
                    message='Do you want to Submit')
    if answer:
        datadisimpan1()
