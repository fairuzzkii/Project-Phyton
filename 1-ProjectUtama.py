import csv
import os
import datetime
import time
import pandas as pd

def Clear():
    os.system('cls')


# ----------------------------------------------------------------------------------------------------------------
# def Tampilan Welcome dan Login
def Welcome():
    Clear()
    file = open("login.txt",mode='r')
    print(file.read())
    pilihan = input(f"{' '*23}{'> Input: '}")
    if pilihan == '0':
        Clear()
        print(f'{"="*30}\n{"Aplikasi telah berhenti":^30}\n{"="*30}')
        exit()
    else:    
        Clear()
        Masuk()
def Masuk():
    Username = input('Masukkan username anda: ')
    Password = input('Masukkan password anda: ')

    dataakun = []

    with open('dataakun.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            dataakun.append({'Id' : row[0], 'Username' : row[1], 'Password' : row[2]})

    Login = []
    for akun in dataakun:
        if Username == akun['Username'] and Password == akun['Password']:
            Login.append(akun)
            Clear()
            print("="*30)
            print(f'{"Anda berhasil masuk":^30}')
            print("="*30)
            input("Tekan [ENTER] untuk melanjutkan!")
            Clear()
            loading_progress()
            HomePage()
    if len(Login) == 0:
        print('Username atau password salah!, Silahkan coba lagi!')
        input("Tekan [ENTER] untuk kembali!")
        Welcome()


def loading_progress(duration=2, steps=100):
    interval = duration / steps
    for i in range(steps + 1):
        progress = i / steps
        bar_length = int(progress * 100)
        bar = "[" + "=" * bar_length + " " * (100 - bar_length) + "]"
        percentage = int(progress * 100)
        print(f"\r{bar} {percentage}%", end="", flush=True)
        time.sleep(interval)
    print("\nLoading complete!")
    time.sleep(1)
    


# ----------------------------------------------------------------------------------------------------------------
# def Homepage
def HomePage():
    Clear()
    file = open("homepage.txt",mode='r')
    print(file.read())
    # print(f'{"="*30}\n{"QUICKSERVE":^30}\n{"="*30}')
    Pilihan = input(f"{' '*23}{'> Masukkan pilihan anda : '}")
    match Pilihan:
        case '0': 
            LogOut()
        case '1':
            Buat_Pesanan()
        case '2' :
            Menu()
        case '3':
            Paket()
        case '4':
            Karyawan()
        case _:
            print("Input salah! Masukkan Input yang sesuai!")
            input("Tekan [ENTER] untuk menginput kembali")
            HomePage()

# ----------------------------------------------------------------------------------------------------------------
# [1] def Buat Pesanan
def Buat_Pesanan():
    Clear()

    print("="*55)
    print(f'{"DAFTAR MENU":^55}')
    print("="*55)
    
    datamenu = []

    with open('datamenu.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datamenu.append([row[0], row[1], row[2], row[3]])

    header_database = ['Id', 'Id_Jenis', 'nama_menu', 'harga']
    data = pd.DataFrame(datamenu, columns=header_database)
    print(data.to_string(index=False))

    print("="*55)
    print(f'{"DAFTAR PAKET":^55}')
    print("="*55)
    

    datapaket = []

    with open('datapaket.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datapaket.append([row[0], row[1],row[2],row[3]])
    header_database = ['Id_paket', 'nama_paket', 'keterangan', 'harga']
    data = pd.DataFrame(datapaket, columns=header_database)
    print(data.to_string(index=False))
    print("="*55)

    Pilihan = input(f'{"[1] Pesan Reguler"}\n{"[2] Pesan Paket"}\n{"[0] Kembali ke Homepage"}\n{"Input: "}')
    match Pilihan:
        case '0':
           HomePage()
        case '1':
            Pesan_reguler()
        case '2':
            Pesan_Paket()
        case _:
            print("Input salah! Masukkan Input yang sesuai!")
            input("Tekan [ENTER] untuk menginput kembali")
            HomePage()

def Pesan_reguler():
    Clear()

    print("="*48)
    print(f'{"DAFTAR MENU":^48}')
    print("="*48)
    

    datamenu = []

    with open('datamenu.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datamenu.append([row[0], row[1], row[2], row[3]])

    header_database = ['Id', 'Id_Jenis', 'nama_menu', 'harga']
    data = pd.DataFrame(datamenu, columns=header_database)
    
    print(data.to_string(index=False))

    pesan = []
    
    while True:
        
        
        pesanan = input(f"\n{'='*48}\n{'Masukkan Pesanan!'}\n{'Tekan [n] untuk selesai'}\n{'Tekan [0] untuk membatalkan pesanan'}\n{'Input : '}").lower()
        
        for i in range(len(datamenu)):
            
                
                
            if datamenu[i][0] == pesanan:
                pesan.append(datamenu[i])
                reguler = pd.DataFrame(pesan, columns=header_database)
                
                
                Clear()
                print("="*48)
                print(f'{"DAFTAR MENU":^48}')
                print("="*48)
                print(f"{data.to_string(index=False)}\n{'='*48}\n{'PESANAN':^48}\n{'='*48}\n{reguler.to_string(index=False)}")
                
                Harga = 0
                for x in reguler['harga']:
                    Harga += int(x)
                print(f"{'-'*48}\n{'Total harga = '}{Harga}\n{'-'*48}\n")    
                          
        
        if pesanan == 'n' and len(pesan) > 0:
            while True:
                Clear()
                print("="*48)
                print(f'{"PEMBAYARAN":^48}')
                print("="*48)
                print(f"Total harga = {Harga}\n{'-'*48}")
                Bayar = input(f"{'Input uang yang masuk !'}\n{'Tekan [0] untuk membatalkan pesanan'}\n{'Input = '}")
                if Bayar.isdigit() == False:
                    print(input('Input tidak valid! Tekan [ENTER] untuk input ulang'))
                elif Bayar == '0':
                    Clear()
                    print("="*48)
                    print(f'{"Pesanan telah dibatalkan":^48}')
                    print("="*48)
                    pesan = []
                    input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
                    Buat_Pesanan()    
                elif int(Bayar) < Harga:
                    print(input('Uang yang dibayarkan kurang! Tekan [ENTER] untuk input ulang'))
                else:
                    Nama_Customer = input("Masukkan nama customer : ")
                    Clear()
                    time = datetime.datetime.now()
                    print("="*48)
                    print(f'{"STRUK PEMBAYARAN":^48}')
                    print("="*48)
                    print (time.strftime("%Y-%m-%d %H:%M"))
                    print(f"NAMA CUSTOMER {':':>3} {Nama_Customer}\n{'PESANAN : '}\n")
                    Struk = reguler.iloc[:,2:]
                    print(Struk.to_string(index=False))
                    print(f"{'-'*48}\n{'TOTAL HARGA '}{':':>5}{' Rp.'}{Harga}\n{'TUNAI'}{':':>12}{' Rp.'}{Bayar}")
                    Kembalian = int(Bayar)-Harga
                    print(f"KEMBALIAN {':':>7} Rp.{Kembalian}\n{'='*48}")
                    input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
                    Buat_Pesanan()
        elif pesanan.isdigit() == False:
            input(f"{'Id tidak valid'}\n{'Tekan [ENTER] untuk input ulang '}")
        
        elif int(pesanan) > int(row[0]):
            input(f"{'Id tidak terdaftar'}\n{'Tekan [ENTER] untuk input ulang '}")   
        elif pesanan == '0':
            Clear()
            print("="*48)
            print(f'{"Pesanan telah dibatalkan":^48}')
            print("="*48)
            pesan = []
            input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
            Buat_Pesanan()

        
        

                    
            
def Pesan_Paket():
    Clear()
    Tampilkan_Paket()
    Opsi = input(f"\n{'-'*55}\n{'Pilih paket yang akan dipesan'}\n{'Tekan [0] untuk kembali'}\n{'Input : '}")
    
    datamenu = []

    with open('datamenu.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datamenu.append([row[0], row[1], row[2], row[3]])
            header_database = ['Id', 'Id_Jenis', 'nama_menu', 'harga']
            menu = pd.DataFrame(datamenu, columns=header_database)

    datapaket = []

    with open('datapaket.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datapaket.append([row[0], row[1],row[2],row[3]])
    header_database = ['Id_paket', 'nama_paket', 'keterangan', 'harga']
    paket = pd.DataFrame(datapaket, columns=header_database)
    pesan = []
    
    if Opsi.isdigit() == False:
        input('Input tidak valid! Tekan [ENTER] untuk input ulang')
        Pesan_Paket()
    elif int(Opsi) > int(row[0]):
        input(f"{'Id tidak terdaftar'}\n{'Tekan [ENTER] untuk input ulang '}")
        Pesan_Paket()
    elif Opsi == '0':
        Buat_Pesanan()


    if Opsi in paket.iloc[:,0].values:
        while True:
            Clear()
            print("="*48)
            print(f'{"DAFTAR MENU":^48}')
            print("="*48)
            print(menu.to_string(index=False))
            print("-"*48)
            pesan = []
            pesan.append(paket.iloc[int(Opsi)-1,1:])
            keterangan = pd.DataFrame(pesan)
            print(keterangan.to_string(index=False))
            input_pesan = input(f"{'-'*48}\n{'Ketikkan menu yang akan dipesan'}\n{'Tekan [0] untuk batalkan pesanan'}\n{'Input : '}")
            if input_pesan == '0':
                Clear()
                print("="*48)
                print(f'{"Pesanan telah dibatalkan":^48}')
                print("="*48)
                pesan = []
                input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
                Buat_Pesanan()
            elif len(input_pesan) == 0:
                print("="*48)
                print(f'{"Pesanan tidak boleh kosong":^48}')
                print("="*48)
                input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
                Pesan_Paket()

            total_harga = int(paket.iloc[int(Opsi)-1,3])
            nama_paket = paket.iloc[int(Opsi)-1,1]
            print(f"Total Harga : {total_harga}")
            Bayar = input(f"{'-'*48}\n{'Ketikkan uang yang masuk!'}\n{'Tekan [0] untuk batalkan pesanan'}\n{'Input: '}")
            if Bayar == '0':
                Pesan_Paket()
            if Bayar.isdigit() == False:
                input('Input tidak valid! Tekan [ENTER] untuk input ulang')
            elif int(Bayar) < total_harga:
                input('Uang yang dibayarkan kurang! Tekan [ENTER] untuk input ulang')
            else:
                break
  
        Nama_Customer = input("Masukkan nama customer : ")
        Clear()
        time = datetime.datetime.now()
        print("="*48)
        print(f'{"STRUK PEMBAYARAN":^48}')
        print("="*48)
        print (time.strftime("%Y-%m-%d %H:%M"))
        print(f"NAMA CUSTOMER {':':>3} {Nama_Customer}\n{'PESANAN '}{': ':>10}{nama_paket}\n{input_pesan}")
        print(f"{'-'*48}\n{'TOTAL HARGA '}{':':>5}{' Rp.'}{total_harga}\n{'TUNAI'}{':':>12}{' Rp.'}{Bayar}")
        Kembalian = int(Bayar) - total_harga
        print(f"KEMBALIAN {':':>7} Rp.{Kembalian}\n{'='*48}")
        input(f"{'Tekan [ENTER] untuk kembali'}\n{'Input: '}")
        Buat_Pesanan()

# ----------------------------------------------------------------------------------------------------------------
# [2] def MENU: tambah menu, update menu, hapus menu
def Tampilkan_Menu():
    Clear()
    
    datamenu = []

    with open('datamenu.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datamenu.append([row[0], row[1], row[2], row[3]])

    header_database = ['Id', 'Id_Jenis', 'nama_menu', 'harga']
    data = pd.DataFrame(datamenu, columns=header_database)
    print("="*48)
    print(f'{"DAFTAR MENU":^48}')
    print("="*48)
    print(data.to_string(index=False))
    print('-'*48)

def Menu() :
    Tampilkan_Menu()
    Pilihan = input(f'{"[1] Tambah Menu"}\n{"[2] Update Menu"}\n{"[3] Hapus Menu"}\n{"[0] Kembali ke Homepage"}\n{"Input: "}')
    match Pilihan:
        case '0':
            HomePage()
        case '1':
            Tambah_Menu()
        case '2':
            Update_Menu()
        case '3':
            Hapus_menu()
        case _:
            print("Input salah! Masukkan Input yang sesuai!")
            input("Tekan [ENTER] untuk menginput kembali")
            Menu()
        
    
def Tambah_Menu():
    Clear()
    datajenis = []

    with open('datajenis.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datajenis.append([row[0], row[1]])
    
    header_database = ['Id_Jenis', 'Jenis']
    data = pd.DataFrame(datajenis, columns=header_database)
    print("="*30)
    print(f'{"JENIS MENU":^30}')
    print("="*30)
    print(data.to_string(index=False))
    print('-'*30)
    id_jenis_baru = input(f"{'Tekan [0] untuk kembali'}\n{'Input Id jenis : '}")
    
    if id_jenis_baru.isdigit() == False:
        input(f"{'Id jenis tidak valid!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Tambah_Menu()
    elif int(id_jenis_baru) > len(datajenis):
        input(f"{'Id jenis tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Tambah_Menu()
    elif id_jenis_baru == '0':
        Menu()
    nama_menu_baru = input('Menu baru: ')
    harga_baru = input("Harga: ")

    if harga_baru.isdigit() == False:
        Clear()
        print("="*30)
        print(f'{"Harga yang diinputkan tidak valid":^30}')
        print("="*30)
        input("Tekan [ENTER] untuk kembali!")
        Tambah_Menu()
    else:
        datamenu = []
    
        with open('datamenu.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                datamenu.append([row[0], row[1], row[2], row[3]])
                Id_baru = int(row[0])

        menu_baru = {'Id_Menu' : Id_baru + 1, 'Id_Jenis' : id_jenis_baru, 'nama_menu' : nama_menu_baru, 'harga' : int(harga_baru)}
        with open('datamenu.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= menu_baru.keys())
            writer.writerow(menu_baru)
        Clear()
        print(f'{"="*30}\n{"Menu berhasil ditambahkan":^30}\n{"="*30}')
        Tawaran = input(f'{"Tambahkan menu lagi?"}\n{"<y/n> "}').lower()
        if Tawaran == 'y':
            Tambah_Menu()
        else:
            Menu()

def Update_Menu():
    Tampilkan_Menu()
    datamenu = []
    datajenis = []
    with open('datajenis.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datajenis.append([row[0], row[1]])
    with open('datamenu.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datamenu.append([row[0], row[1], row[2], row[3]])  
    id_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Input Id yang diupdate : '}")
    if id_edit == '0':
        Menu()
    elif id_edit.isdigit() == False:
        input(f"{'Id menu tidak valid!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Update_Menu()
    elif int(id_edit) > int(row[0]):
        input(f"{'Id menu tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Update_Menu()        
    jenis_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Input Id jenis baru : '}")
    
    if jenis_edit.isdigit() == False:
        input(f"{'Id jenis tidak valid!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Update_Menu()
    
    elif int(jenis_edit) > len(datajenis):
        input(f"{'Id jenis tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Update_Menu()
    elif jenis_edit == '0':
        Menu()
    menu_edit = input("Nama menu baru: ")
    harga_edit = input("Harga baru: ")        
        
    for i in range(len(datamenu)):    
            if datamenu[i][0] == id_edit:
                datamenu[i][1] = jenis_edit
                datamenu[i][2] = menu_edit
                datamenu[i][3] = int(harga_edit)
    with open("datamenu.csv", mode="w", newline="")as file:
        write = csv.writer(file)
        write.writerows(datamenu)
    Clear()
    print(f'{"="*30}\n{"Menu berhasil diupdate":^30}\n{"="*30}')
    Entri = input(f'{("Apakah anda ingin mengupdate menu lagi?")}\n{("<y/n> ")}').lower()
    if Entri == "y":
        Update_Menu()
    else:
        Menu()

def Hapus_menu():
    Tampilkan_Menu()
    datamenu = []                                             
    with open("datamenu.csv", "r", newline="") as file:    
                csv_reader = csv.reader(file)
                for row in csv_reader:                                    
                    datamenu.append([row[0], row[1], row[2], row[3]])    
    Hapus_id= input(f"{'Tekan [0] untuk kembali'}\n{'Input Id yang dihapus : '}")
    if Hapus_id.isdigit() == False or int(Hapus_id) > int(row[0]):
        input(f"{'Id menu tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Hapus_menu()
    elif Hapus_id == '0':
        Menu()
    i = 0
    for data_baris in datamenu:
        if data_baris[0] == Hapus_id:
            datamenu.pop(i)
        i += 1
    
    with open("datamenu.csv", "w", newline="") as file:    
        csv_writer = csv.writer(file)                          
        csv_writer.writerows(datamenu)
    Clear()
    print(f'{"="*30}\n{"Menu berhasil dihapus":^30}\n{"="*30}')
    Tawaran = input(f'{"Hapus menu lagi?"}\n{"<y/n> "}').lower()
    if Tawaran == 'y':
        Hapus_menu()
    else:
        Menu()

# ----------------------------------------------------------------------------------------------------------------
# [3] def PAKET:Tambah paket, update paket, hapus paket    
def Tampilkan_Paket():
    

    datapaket = []

    with open('datapaket.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datapaket.append([row[0], row[1],row[2],row[3]])
    header_database = ['Id_paket', 'nama_paket', 'keterangan', 'harga']
    data = pd.DataFrame(datapaket, columns=header_database)
    print(f'{"="*55}\n{"DAFTAR PAKET":^55}\n{"="*55}')
    print(data.to_string(index=False))
    print('-'*55)

def Paket():
    Clear()
    Tampilkan_Paket()
    Pilihan = input(f'{"[1] Tambah Paket"}\n{"[2] Update Paket"}\n{"[3] Hapus Paket"}\n{"[0] Kembali ke Homepage"}\n{"Input: "}')
    match Pilihan:
        case '0':
            HomePage()
        case '1':
            Tambah_Paket()
        case '2':
            Update_Paket()
        case '3':
            Hapus_Paket()
        case _:
            print("Input salah! Masukkan Input yang sesuai!")
            input("Tekan [ENTER] untuk menginput kembali")
            Paket()
          

def Tambah_Paket():
    Clear()
    Tampilkan_Paket()
    
    nama_paket_baru = input(f"{'Tekan [0] untuk kembali'}\n{'Paket baru : '}")
    if nama_paket_baru == '0':
        Paket()
    keterangan_baru = input(f"{'Tekan [0] untuk kembali'}\n{'Keterangan paket : '}")
    if keterangan_baru == '0':
        Paket()
    harga_baru = input(f"{'Tekan [0] untuk kembali'}\n{'Harga : '}")
    if harga_baru == '0':
        Paket()
    if harga_baru.isdigit() == False:
        Clear()
        print("="*30)
        print(f'{"Harga yang diinputkan tidak valid":^30}')
        print("="*30)
        input("Tekan [ENTER] untuk kembali!")
        Tambah_Paket()    
    else:
        datapaket = []

        with open('datapaket.csv', mode='r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                datapaket.append([row[0], row[1], row[2], row[3]])
                Id_baru = int(row[0])

        paket_baru = {'Id_Paket' : Id_baru + 1,  'nama' : nama_paket_baru, 'keterangan': keterangan_baru, 'harga' : int(harga_baru)}
        with open('datapaket.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames= paket_baru.keys())
            writer.writerow(paket_baru)
        Clear()
        print(f'{"="*30}\n{"Paket berhasil ditambahkan":^30}\n{"="*30}')
        Tawaran = input(f'{"Tambahkan paket lagi?"}\n{"<y/n> "}').lower()
        if Tawaran == 'y':
            Tambah_Paket()
        else:
            Paket()

def Update_Paket():
    Clear()
    Tampilkan_Paket()
    datapaket = []
    with open('datapaket.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            datapaket.append([row[0], row[1], row[2], row[3]])
    Idpaket_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Id paket yang diupdate : '}")
    if Idpaket_edit.isdigit() == False or int(Idpaket_edit) > int(row[0]):
        input(f"{'Id paket tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Update_Paket()
    elif Idpaket_edit == '0':
        Paket()
    paket_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Nama paket baru : '}")
    if paket_edit == '0':
        Paket()
    keterangan_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Keterangan baru paket : '}")
    if keterangan_edit == '0':
        Paket()
    harga_edit = input(f"{'Tekan [0] untuk kembali'}\n{'Harga baru paket : '}")
    if harga_edit == '0':
        Paket()
    
    if harga_edit.isdigit() == False:
        input(f"{'Harga yang diinputkan tidak valid!'}\n{'tekan [ENTER] untuk input ulang '}")
        Update_Paket()
    else:    
        for i in range(len(datapaket)):
            if datapaket[i][0] == Idpaket_edit:
                datapaket[i][1] = paket_edit
                datapaket[i][2] = keterangan_edit
                datapaket[i][3] = int(harga_edit)

    with open('datapaket.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datapaket)
    
    Clear()
    print(f'{"="*30}\n{"Paket berhasil diupdate":^30}\n{"="*30}')
    Tawaran = input(f'{("Apakah anda ingin mengupdate paket lagi?")}\n{("<y/n> ")}').lower()
    if Tawaran == "y":
        Update_Paket()
    else:
        Paket()

def Hapus_Paket():       
    Clear()
    Tampilkan_Paket()
    datapaket = []                                             
    with open("datapaket.csv", "r", newline="") as file:    
                csv_reader = csv.reader(file)
                for row in csv_reader:                                    
                    datapaket.append([row[0], row[1], row[2], row[3]])    
    Hapus_id= input(f"{'Tekan [0] untuk kembali'}\n{'Id paket yang dihapus : '}")
    if Hapus_id.isdigit() == False or int(Hapus_id) > int(row[0]):
        input(f"{'Id paket tidak terdaftar!'}\n{'Tekan [ENTER] untuk input ulang '}")
        Paket()
    elif Hapus_id == '0':
        Paket()
    i = 0
    for data_baris in datapaket:
        if data_baris[0] == Hapus_id:
            datapaket.pop(i)
        i += 1
    
    with open("datapaket.csv", "w", newline="") as file:    
        csv_writer = csv.writer(file)                          
        csv_writer.writerows(datapaket)
    
    Clear()
    print(f'{"="*30}\n{"Paket berhasil dihapus":^30}\n{"="*30}')
    Tawaran = input("Hapus paket lagi? (y/n): ").lower()
    if Tawaran == 'y':
        Hapus_Paket()
    else:
        Paket()

# ----------------------------------------------------------------------------------------------------------------
# [4] def PROFIL KARYAWAN: tampilan karyawan dan register karyawan
def Karyawan():
    Clear()

    dataakun = []

    with open('dataakun.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            dataakun.append([row[0], row[1]] )

    header_database = ["Id", "Akun terdaftar"]
    data = pd.DataFrame(dataakun, columns=header_database)
    print(f'{"="*30}\n{"DAFTAR KARYAWAN":^30}\n{"="*30}')

    print(data.iloc[1:,:].to_string(index=False))
    print('-'*30)
    Pilihan = input(f'{"[1] Register Karyawan"}\n{"[2] Hapus Karyawan"}\n{"[0] Kembali ke Homepage"}\n{"Input: "}')
    match Pilihan:
        case '1':
            Register()
        case '2':
            Hapus_Karyawan()
        case '0':
            HomePage()
        case _:
            print("Input salah! Masukkan Input yang sesuai!")
            input("Tekan [ENTER] untuk menginput kembali")
            Karyawan()
            

def Register():
    Clear()
    dataakun = []
    Username = input(f"{'Tekan [0] untuk kembali'}\n{'Masukkan username baru : '}")
    if Username == '0':
        Karyawan()
    Password = input(f"{'Tekan [0] untuk kembali'}\n{'Masukkan password baru : '}")
    if Password == '0':
        Karyawan()
    with open('dataakun.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            dataakun.append({'Id' : row[0], 'Username' : row[1], 'Password' : row[2]})
        Id_karyawan = int(row[0])

    Username_Ada = False

    for akun in dataakun:
        if Username == akun['Username']:
            print('Username sudah ada, Masukkan username lain')
            input("Tekan [ENTER] untuk kembali")
            Karyawan()
            Username_Ada = True
            
    Clear()
    if Username_Ada == False:
        if len(Username) < 1:
            print("Username tidak boleh kosong")
            input("Tekan [ENTER] untuk kembali")
            Karyawan()
        if Password.isalnum() == False:
            print("Password harus terdiri dari huruf dan angka")
            input("Tekan [ENTER] untuk kembali")
            Karyawan()
        elif len(Password) < 8:
            print("Password minimal harus 8 karakter")
            input("Tekan [ENTER] untuk kembali")
            Karyawan()
        else:
            databaru = {'Id' : Id_karyawan +1, 'username' : Username, 'password' : Password}
            with open('dataakun.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames= databaru.keys())
                writer.writerow(databaru)

            print(f'{"="*30}\n{"Karyawan berhasil ditambahkan":^30}\n{"="*30}')
            Tawaran = input("Tambahkan karyawan lagi? (y/n): ").lower()
            if Tawaran == 'y':
                Register()
            else:
                Karyawan()

def Hapus_Karyawan():
    Hapus = input("Id karyawan yang akan dihapus: ")       
    
    dataakun = []

    with open('dataakun.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            dataakun.append([row[0], row[1]] )
    
    if Hapus.isdigit() == False:
        input(f"{'Id karyawan tidak valid!'}\n{'Tekan [ENTER] untuk kembali'}")
        Karyawan()
    elif int(Hapus) > int(row[0]):
        input(f"{'Id karyawan tidak terdaftar!'}\n{'Tekan [ENTER] untuk kembali'}")
        Karyawan()
    Tempat_Id = []                                             
    with open("dataakun.csv", "r", newline="") as file:    
                csv_reader = csv.reader(file)
                for row in csv_reader:                                    
                    if row[0] != Hapus:                             
                        Tempat_Id.append(row)                          
    with open("dataakun.csv", "w", newline="") as file:    
        csv_writer = csv.writer(file)                          
        csv_writer.writerows(Tempat_Id)
    Clear()
    print(f'{"="*30}\n{"Akun karyawan berhasil dihapus":^30}\n{"="*30}')
    Tawaran = input("Hapus karyawan lagi? (y/n): ").lower()
    if Tawaran == 'y':
        Hapus_Karyawan()
    else:
        Karyawan()                      

# ----------------------------------------------------------------------------------------------------------------
# [0] def log out
def LogOut():
    Clear()
    print(f'{"="*30}\n{"Anda telah logout":^30}\n{"="*30}')
    input("tekan [ENTER] untuk melanjutkan!")
    Welcome()

# Start-----------------------------------------------------------------------------------------------------------      

Welcome()