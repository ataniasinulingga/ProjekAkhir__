import csv
import pwinput
from prettytable import PrettyTable
import os
os.system ("cls")


# Dictionary
useradmin = {'Name' : 'jaka','Password' : '123'}

uang_pelanggan = {"Uang" : 0,"Saldo" : 0,"Saldo_topup" :0}

# Prettytable Makanan
tabel_menu = PrettyTable()
tabel_menu.field_names = ["Kode Menu", "Nama Menu", "Harga Menu"]

# menu_makanan dictionary
menu_makanan = {
    "01": {"Nama Menu": "Ikan Gurame", "Harga Menu": "Rp. 60.000"},
    "02": {"Nama Menu": "Rendang", "Harga Menu": "Rp. 40.000"},
    "03": {"Nama Menu": "Sop Iga Sapi", "Harga Menu": "Rp. 35.000"},
    "04": {"Nama Menu": "Nila Goreng", "Harga Menu": "Rp. 30.000"},
    "05": {"Nama Menu": "Lalapan Ayam Bakar", "Harga Menu": "Rp. 25.000"},
    "06": {"Nama Menu": "Soto Ayam Lamongan", "Harga Menu": "Rp. 25.000"},
    "07": {"Nama Menu": "Rawon", "Harga Menu": "Rp. 25.000"},
    "08": {"Nama Menu": "Bakso", "Harga Menu": "Rp. 20.000"},
    "09": {"Nama Menu": "Nasi Goreng", "Harga Menu": "Rp. 15.000"},
    "10": {"Nama Menu": "Indomie Telor", "Harga Menu": "Rp. 12.000"}
}


# Masukkan menu ke prettytable
for kode_menu, menu_info in menu_makanan.items():
    tabel_menu.add_row([kode_menu, menu_info["Nama Menu"], menu_info["Harga Menu"]])

# Prettytable Minuman
tabel_minum = PrettyTable()
tabel_minum.field_names = ["Kode Minuman", "Nama Minuman", "Harga Minuman"]

# Dictionary menu_minuman
menu_minuman = {
    "01": {"Nama Minuman": "Es Teh Manis", "Harga Minuman": "Rp. 5.000"},
    "02": {"Nama Minuman": "Es Jeruk", "Harga Minuman": "Rp. 6.000"},
    "03": {"Nama Minuman": "Jeruk Hangat", "Harga Minuman": "Rp. 6.000"},
    "04": {"Nama Minuman": "Teh Panas", "Harga Minuman": "Rp. 5.000"},
    "05": {"Nama Minuman": "Milo", "Harga Minuman": "Rp. 10.000"},
    "06": {"Nama Minuman": "Jus Alpukat", "Harga Minuman": "Rp. 18.000"},
    "07": {"Nama Minuman": "Jus Mangga", "Harga Minuman": "Rp. 17.000"},
    "08": {"Nama Minuman": "Air Mineral", "Harga Minuman": "Rp. 4.000"},
    "09": {"Nama Minuman": "Lychee Tea", "Harga Minuman": "Rp. 10.000"},
    "10": {"Nama Minuman": "Lemon Tea", "Harga Minuman": "Rp. 10.000"}
}

# Masukin Minuman ke prettytable
for kode_minuman, minuman_info in menu_minuman.items():
    tabel_minum.add_row([kode_minuman, minuman_info["Nama Minuman"], minuman_info["Harga Minuman"]])


# DATABASE
# User (Pembeli)
with open('user_database.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["User", "Password","Saldo"])

# Save tabel_menu ke CSV
with open('menu_makanan.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Kode Menu", "Nama Menu", "Harga Menu"])
    for row in menu_makanan:
        writer.writerow(row)

# Save tabel_minum ke CSV
with open('menu_minuman.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Kode Minuman", "Nama Minuman", "Harga Minuman"])
    for row in menu_minuman:
        writer.writerow(row)

#Registrasi Pelanggan
def register():
    while True:
        User = input("Masukkan nama user: ")
        Password = pwinput.pwinput("Masukkan password: ")

        # Mencegah user dengan nama user sama
        with open('user_database.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == User:
                    print("Nama user yang anda gunakan sudah dipakai.")
                    return

        # Input saldo awal
        try:
            saldo_awal = int(input("Masukkan saldo awal Anda: Rp. "))
        except ValueError:
                print("Masukkan jumlah yang valid (angka).")
                continue

        # Inisialisasi orderan dan keuangan
        user = {
            'Name': User,
            'Password': Password,
            'order': [],
            'uang_pelanggan': {'Saldo': saldo_awal, 'Saldo_topup': 0}
        }
        print(f"Registrasi berhasil! Saldo awal Anda: Rp. {saldo_awal}")

        # Save user data to user_database.csv
        with open('user_database.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([User, Password, saldo_awal])

        return user


        
# Menu Top up
def top_up(user):
    while True:
        try:
            amount = int(input("Masukkan jumlah saldo yang ingin ditambahkan (Rp.): "))
        except ValueError:
            print("Masukkan jumlah saldo yang valid (angka).")
            continue

        if amount <= 0:
            print("Jumlah saldo harus lebih dari 0.")
        else:
            user['uang_pelanggan']['Saldo'] += amount
            user['uang_pelanggan']['Saldo_topup'] += amount
            print(f"Saldo berhasil ditambahkan. Saldo sekarang: Rp. {user['uang_pelanggan']['Saldo']}")
            break

#Login Pelanggan
def login():
    Username = input("Enter your username: ")
    Password = pwinput.pwinput("Enter your password: ")

    with open('user_database.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row and row[0] == Username and row[1] == Password:
                print("Login berhasil! Selamat datang, " + Username + "!")
                user = {'Name': Username, 'Password': Password, 'order': [], 'uang_pelanggan': {'Saldo': 0, 'Saldo_topup': 0}}
                return user  # Return the user dictionary

    print("Login gagal! Username atau password salah.")
    return None
# Transaksi
def transaksi(user):
    while True:
        print("DAFTAR MENU YANG READY")
        read_admin()
        print("1. Menu Makanan")
        print("2. Menu Minuman")
        print("3. Lihat Keranjang")
        print("4. Checkout")
        print("5. Top up")
        print("6. Kembali")

        choice_pelanggan = input("Apa yang ingin anda pesan?: ")

        if choice_pelanggan == "1":
            # Menu Makanan
            print(tabel_menu)
            kode_makanan = input("Masukkan kode makanan yang ingin diorder: ")
            try:
                jumlah = int(input("Masukkan jumlah yang ingin diorder: "))
            except ValueError:
                print("Masukkan jumlah yang valid (angka).")
                continue

            # Check if the entered menu code exists
            if kode_makanan in menu_makanan:
                # Add the item to the customer's order
                user['order'].append([kode_makanan, jumlah])
                print("Item ditambahkan ke keranjang.")
            else:
                print("Kode makanan tidak valid. Silakan coba lagi.")

        elif choice_pelanggan == "2":
            # Menu Minuman
            print(tabel_minum)
            kode_minuman = input("Masukkan kode minuman yang ingin diorder: ")
            try:
                jumlah = int(input("Masukkan jumlah yang ingin diorder: "))
            except ValueError:
                print("Masukkan jumlah yang valid (angka).")
                continue

            # Check if the entered menu code exists
            if kode_minuman in menu_minuman:
                # Add the item to the customer's order
                user['order'].append([kode_minuman, jumlah])
                print("Item ditambahkan ke keranjang.")
            else:
                print("Kode minuman tidak valid. Silakan coba lagi.")

        elif choice_pelanggan == "3":
            # Lihat Keranjang
            print("Keranjang Belanja Anda:")
            for item in user['order']:
                kode_item = item[0]
                jumlah = item[1]
                item_info = [v for k, v in menu_makanan.items() if k == kode_item][0]
                print(f"{item_info['Nama Menu']} (Qty: {jumlah})")

        elif choice_pelanggan == "4":
            # Checkout
            total_harga = 0
            print("Keranjang Belanja Anda:")
            for item in user['order']:
                kode_item = item[0]
                jumlah = item[1]
                item_info = [v for k, v in menu_makanan.items() if k == kode_item][0]
                item_name = item_info['Nama Menu']
                harga = int(item_info["Harga Menu"].split()[-1].replace(".", ""))
                total_harga_item = harga * jumlah
                total_harga += total_harga_item
                print(f"{item_name} (Qty: {jumlah}) - Rp. {total_harga_item}")

            if user['uang_pelanggan']['Saldo'] < total_harga:
                print("Saldo Anda tidak mencukupi untuk melakukan transaksi.")
            else:
                user['uang_pelanggan']['Saldo'] -= total_harga
                print(f"Total Harga: Rp. {total_harga}")
                print(f"Sisa Saldo: Rp. {user['uang_pelanggan']['Saldo']}")
                print("Berhasil Order!!! Terima kasih atas pesanan Anda!!")
                print("Pesanan akan segera diantar..")
                break
            # Mengkosongkan orderan tadi
            user['order'] = []

        elif choice_pelanggan == "5":
            top_up(user)
        elif choice_pelanggan == "6":
            return

        else:
            print("Pilihan tidak valid.")
            print("+" * 41)
            print("++                                     ++")
            print("++  TERIMA KASIH SUDAH MEMBELI DISINI  ++")
            print("++                                     ++")
            print("+" * 41)
            print(" ")


# admin CRUD
# CREATE
def create_admin():
    while True:
        print("1. Menu makanan")
        print("2.Menu Minuman")
        print("3.Kembali")
        choice_admin = input("Menu makanan/minuman : ")

        if choice_admin == "1":
            kode_menu = input("Masukkan kode menu: ")
            nama_menu = input("Masukkan nama menu: ")
            harga_menu = input("Masukkan harga menu: ")

            # Masukkan ke Prettytable Makanan
            new_menu_item = {"Nama Menu": nama_menu, "Harga Menu": harga_menu}
            menu_makanan[kode_menu] = new_menu_item
            tabel_menu.add_row([kode_menu, new_menu_item["Nama Menu"], new_menu_item["Harga Menu"]])  

            print("Menu berhasil ditambahkan.")
        # Buat yang minuman :
        elif choice_admin == "2":
            kode_minuman = input("Masukkan kode menu: ")
            nama_minuman = input("Masukkan nama menu: ")
            harga_minuman = input("Masukkan harga menu: ")

            #Masukkan ke Prettytable Minuman
            minuman_baru = {"Nama Minuman": nama_minuman, "Harga Minuman": harga_minuman}
            menu_minuman[kode_minuman] = minuman_baru
            tabel_minum.add_row([kode_minuman, minuman_baru["Nama Minuman"], minuman_baru["Harga Minuman"]])  

            print("Menu berhasil ditambahkan.")
        
        elif choice_admin == "3":
            break
        else:
            print("Menu tidak tersedia.")

# READ (BACA MENU YANG ADA)
def read_admin():
    print("Daftar Menu Makanan dan Minuman:")
    print(tabel_menu)
    print(tabel_minum)

# UPDATE
def update_admin():
    while True:
        print("1. Menu makanan")
        print("2.Menu Minuman")
        print("3.Kembali")
        choice_admin2 = input("Menu makanan/minuman : ")

        if choice_admin2 == "1" :
            kode_menu = input("Masukkan kode menu yang ingin diperbarui: ")

            if kode_menu in menu_makanan:
                menu_makanan[kode_menu]["Nama Menu"] = input("Masukkan nama menu baru: ")
                menu_makanan[kode_menu]["Harga Menu"] = input("Masukkan harga menu baru: ")
                print("Menu berhasil diperbarui.")
    
                # mengupdate prettytable makanan
                for row in tabel_menu.rows:
                    if kode_menu == row[0]:
                        row[1] = menu_makanan[kode_menu]["Nama Menu"]
                        row[2] = menu_makanan[kode_menu]["Harga Menu"]
            else:
                print("Menu tidak ditemukan.")
        #Opsi jika milih minuman
        elif choice_admin2 == "2":
            kode_minuman = input("Masukkan kode menu yang ingin diperbarui: ")

            if kode_minuman in menu_makanan:
                menu_minuman[kode_minuman]["Nama Minuman"] = input("Masukkan nama menu baru: ")
                menu_minuman[kode_minuman]["Harga Menu"] = input("Masukkan harga menu baru: ")
                print("Menu berhasil diperbarui.")
    
                # mengupdate isi prettytablenya minum
                for row in tabel_minum.rows:
                    if kode_minuman == row[0]:
                        row[1] = menu_minuman[kode_minuman]["Nama Menu"]
                        row[2] = menu_minuman[kode_minuman]["Harga Menu"]
            else:
                print("Menu tidak ditemukan.")

        elif choice_admin2 == "3":
            break
        else:
            print("Menu tidak tersedia.")



# DELETE
def delete_admin():
    while True:
        print("1. Menu makanan")
        print("2.Menu Minuman")
        print("3.Kembali")
        choice_admin3 = input("Menu makanan/minuman : ")

        if choice_admin3 == "1":
            kode_makanan = input("Masukkan kode menu yang ingin dihapus: ")

            if kode_makanan in menu_makanan:
                del menu_makanan[kode_makanan]
                
                # Menghapus baris tertentu sesuai permintaan di prettytable makanan
                for i, row in enumerate(tabel_menu.rows):
                    if kode_makanan == row[0]:
                        tabel_menu.del_row(i)
                print("Menu dihapus.")
            else:
                print("Menu tidak ditemukan.")
        #Opsi jika milih minuman
        elif choice_admin3 == "2":
            kode_minuman = input("Masukkan kode menu yang ingin dihapus: ")

            if kode_minuman in menu_minuman:
                del menu_minuman[kode_minuman]
                
                # Menghapus baris tertentu sesuai permintaan di prettytable minuman
                for i, row in enumerate(tabel_minum.rows):
                    if kode_minuman == row[0]:
                        tabel_minum.del_row(i)
                print("Menu dihapus.")
            else:
                print("Menu tidak ditemukan.")
        
        elif choice_admin3 == "3":
            break
        else:
            print("Menu tidak tersedia.")



# Main Program
while True :
    print("="*41)
    print("|                                       |")
    print("|    Selamat Datang di Nusantara's!!!   |")
    print("|                                       |")
    print("="*41)
    print(" ")
    # Input Pengguna (1/2/3)
    print ("1. Admin (login) ")
    print ("2. Pembeli ")
    print ("3. Keluar ")
    print(" ")
    status = input("Siapa anda??? : ")



# Jika masuk sbg Admin
    if status == "1":
        # jumlah percobaan login
        max_attempts = 3
        attempts = 0
        logged_in = False
        while attempts < max_attempts:
            user = input("Masukkan username anda : ")
            pw = pwinput.pwinput("Masukkan password anda : ")
            if user == useradmin['Name'] and pw == useradmin['Password']:
                print("Selamat anda telah masuk!!!")
                logged_in = True
                break
            else:
                print("Username atau password yang dimasukkan salah!")
                attempts += 1
                if attempts < max_attempts:
                    print(f"Kamu punya {max_attempts - attempts} kesempatan untuk mencoba lagi")
                else:
                    print("Percobaan habis. Kembali")
                    break
        if not logged_in:  
            continue

        while True:
            print("+"*40)
            print("Admin Nusantara's")
            print("+"*40)
            print("1. Tambah Menu")
            print("2. Lihat Menu")
            print("3. Update Menu")
            print("4. Hapus Menu")
            print("5. Kembali")
            admin_choice = input("Pilih menu: ")
            if admin_choice == "1" :
                create_admin()
            elif admin_choice == "2":
                read_admin()
            elif admin_choice == "3":
                update_admin()
            elif admin_choice == "4":
                delete_admin()
            elif admin_choice == "5":
                break  # Exit the admin menu loop and go back to the main menu
            else:
                print("Menu tidak tersedia")

#Jika masuk sebagai pelanggan

    elif status == "2":
        while True:
            print("1. Login akun yang sudah ada")
            print("2. Register (Pengguna baru)")
            print("3. Kembali ")
            choice_pelanggan = input("Login / Register ? : ")

            if choice_pelanggan == "1":
                user = login()
                if user:
                    transaksi(user)  # Masuk ke transaksi

            elif choice_pelanggan == "2":
                user = register()
                if user:
                    transaksi(user)  # Masuk ke transaksi
                break

            elif choice_pelanggan == "3":
                break  # buat balik ke opsi login/regis
            else:
                print("Menu tidak tersedia")

    # Opsi KELUAR
    elif status == "3":
        print("Terima kasih telah mengunjungi resto kami!!.")
        break  # Buat keluar program
    else :
        print("Masukkan anda tidak valid!")
        print("Masukkan input yang benar!")
        continue #Jadi tetap lanjut program,disuruh input ulang