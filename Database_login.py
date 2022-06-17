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

#Halaman Pertama
def firstscreen():
    global mybutton1,mybutton2,mylabel1

    mylabel1 = Label(text="Stasiun SojoPurbaja", borderwidth=4, bg="Light Green")
    mylabel1.pack()
    mybutton1 = Button(screen, 
                  text='Register',
                  borderwidth=2,
                  command=register,
                  bg = '#296d98',
                  fg = 'white'  )
    mybutton1.pack()

    mybutton2 = Button(screen,
                  text='Login',
                  borderwidth = 2,
                  command = login,
                  bg = '#296d98',
                  fg = 'white'  )
    mybutton2.pack()

def menujupilihkeretascreen():
    global Username,Password
    Username = euser.get()
    Password= epass.get()
    pilihkeretascreen()

def clearscreen1():
    bt_kembali1.pack_forget()
    bt_kembali2.pack_forget()
    e1.pack_forget()
    e2.pack_forget()
    e3.pack_forget()
    e4.pack_forget()
    e5.pack_forget()
    e6.pack_forget()
    e7.pack_forget()
    e8.pack_forget()
    mylabela.pack_forget()
    mylabelb.pack_forget()
    mylabelc.pack_forget()
    mylabeld.pack_forget()
    mylabele.pack_forget()
    mylabelf.pack_forget()
    mylabelg.pack_forget()
    mylabelh.pack_forget()

    firstscreen()

#Tampilan Home dan Tampilan Kursi
def pilihkeretascreen():
    euser.pack_forget()
    mylabel1.pack_forget()
    mylabel2.pack_forget()
    epass.pack_forget()
    bt_kembali1.pack_forget()
    bt_kembali2.pack_forget()

    global search,kereta,list_kereta,tujuan,searchbutton,bck_btn1

    list_kereta= pd.read_csv('kereta.csv')
    kereta = pd.DataFrame(list_kereta)

    tujuan = (kereta["kota_tujuan"])
    daftartujuan = tujuan.tolist()

    search= ttk.Combobox(screen1, values=daftartujuan, state="readonly")
    search.pack()
    searchbutton= Button(screen1,text="Cari" ,command=fg)
    searchbutton.pack()
    bck_btn1=Button(screen1, text="Quit",command=quit)
    bck_btn1.pack()
def fg():
    global search_kereta,lockereta,cari,tujuan_kota
    bck_btn1.pack_forget()
    search_kereta = kereta[kereta['kota_tujuan']==search.get()].index.item()
    lockereta = kereta.loc[search_kereta].tolist()
    tujuan_kota= lockereta[2]
    cari=Button(screen1, text=lockereta,command=tampilkursi)
    cari.pack()

def tampilkursi():
    search.pack_forget()
    searchbutton.pack_forget()
    cari.pack_forget()
    global kursiavailable,kursiavb_btn,id,harga,bck_btn

    seat = ['A1', 'A2', 'A3', 'A4', 
        'B1', 'B2', 'B3', 'B4', 
        'C1', 'C2', 'C3', 'C4', 
        'D1', 'D2', 'D3', 'D4', 
        'E1', 'E2', 'E3', 'E4', 
        'F1', 'F2', 'F3', 'F4', 
        'G1', 'G2', 'G3', 'G4', 
        'H1', 'H2', 'H3', 'H4', 
        'I1', 'I2', 'I3', 'I4', 
        'J1', 'J2', 'J3', 'J4', 
        'K1', 'K2', 'K3', 'K4', 
        'L1', 'L2', 'L3', 'L4']
    
    id = lockereta[0]
    harga= lockereta[4]
    cek_kursi= pd.read_csv('data_pembelian.csv')
    cek_kursi1 = cek_kursi.loc[cek_kursi["Kereta"] == id, "KodeKursi"]
    cek_harga=cek_kursi.loc[cek_kursi["Harga"] == harga, "Harga"]
    list_kursi = cek_kursi1.tolist()
    print(list_kursi)
    for i in list_kursi:
        for j in seat:
            if i == j:
                print(j)
                seat.remove(j)
           
    kursiavailable= ttk.Combobox(screen1, values=seat, state="readonly")
    kursiavailable.pack()
    kursiavb_btn=Button(screen1, text="Pilih Kursi",command=message5)
    kursiavb_btn.pack()
    bck_btn=Button(screen1, text="Kembali",command=bck)
    bck_btn.pack()        

#Penyimpanan Data 
def datadisimpan1(): 
    global kursi_dipilih,ktp,userData,df1,nama
    kursi_dipilih= kursiavailable.get()
    
    userData = pd.read_csv('DatabaseAkun.csv')
    df1= pd.DataFrame(userData)

    search_akun = df1[df1['Username']==euser.get()].index.item()
    akun = df1.loc[search_akun].tolist()
    ktp= akun[3]
    nama= akun[2]
    matching_creds = (len(df1[(df1.Username == Username) & (df1.Password == Password)]) > 0)
    if matching_creds:
        simpan_data = pd.read_csv('data_pembelian.csv')
        bl= pd.DataFrame(simpan_data)   
        newbeli = {'NomorKTP' : [ktp],
                        'Kereta' : [id],
                        'KodeKursi' : [kursi_dipilih],
                        'Harga' : [harga]}
        pembelian = pd.DataFrame(newbeli)
        pembelian.to_csv('data_pembelian.csv', mode='a', index=False, header=False)
        output()
def output():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial","B", size=14)
    pdf.cell(200,10, txt='Stasiun SojopurBaja', ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(100,10, txt="Nama Pembeli: {}".format(nama),ln=2, align="L")
    pdf.cell(100,10, txt="No KTP: {}".format(ktp), ln=2, align="L")
    pdf.cell(100,10, txt="Tujuan: {}".format(tujuan_kota), ln=2, align="L")        
    pdf.cell(100,10, txt="Kursi Yang dipilih: {}".format(kursi_dipilih), ln=2, align="L")
    pdf.cell(100,10, txt="Total Bayar: {}".format(harga), ln=1, align="C")
    pdf.output("{}\\TIKET.pdf".format(dir_path))
    
    quit_btn=Button(screen1, text="Quit",command=quit)
    quit_btn.pack()
def quit():
    screen.destroy()
#----

firstscreen()
screen.mainloop()