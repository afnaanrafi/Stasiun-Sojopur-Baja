import csv
import pandas as pd

database= []
def login():
    userData = pd.read_csv('Database_Akun.csv')
    df = pd.DataFrame(userData)
    
    global Username
    global Password
    
    Username=e1.get()
    Password=e2.get()
 
    matching_creds = (len(df[(df.username == Username) & (df.password == Password)]) > 0)

    if matching_creds:
        print('success')
        clearscreen("first")
    else:
        print('\nYour account is not registered yet!')
        print('please contact admin')

def register():
    userData = pd.read_csv('Database_Akun.csv')
    df = pd.DataFrame(userData)

    global Username
    global Password
    Username = e1.get()
    Password= e2.get()
    Nama_Lengkap= e3.get()
    Nomor_KTP = e4.get()
    Email = e5.get()
    No_Telp = e6.get()
    Tanggal_Lahir = e7.get()
    Jenis_Kelamin = e8.get()

    matching_creds = (len(df[(df.username == Username) ]) < 1 or len(df[(df.nomor == Password) ]) < 1)

    if matching_creds and Username != "":
        print('success')
        newuser = {'Username' : [Username],
                'Password' : [Password],
                'Nama Lengkap' : [Nama_Lengkap],
                'Nomor KTP' : [Nomor_KTP],
                'Email' : [Email],
                'Nomor Telpon' : [No_Telp],
                'Tanggal Lahir' : [Tanggal_Lahir],
                'Jenis Kelamin' : [Jenis_Kelamin],}
        registeruser = pd.DataFrame(newuser)
        registeruser.to_csv('Database_Akun.csv', mode='a', index=False, header=False)
        clearscreen("first")
    else:
        print('Username or number already exist')
