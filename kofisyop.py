import csv
import pwinput
import os
import sys
import time
from prettytable import PrettyTable
from datetime import datetime

os.system("cls")

print("\n------------------------------------------")
print("        Selamat Datang di Kofisyop")
print("------------------------------------------")

#file csv
csv_user = "users.csv"
csv_menu = "menu.csv"

#tabel menu utama
def tabel_menu_utama():
    pilihan_login = PrettyTable()
    pilihan_login.field_names = ["No.", "Pilihan"]
    pilihan_login.add_row(["1.", "Register"])
    pilihan_login.add_row(["2.", "Login"])
    pilihan_login.add_row(["3.", "Logout"])
    print(pilihan_login)

#tabel fitur fitur_kasir
def tabel_fitur_kasir():
    fitur_kasir = PrettyTable()
    fitur_kasir.field_names = ["No.", "Fitur"]
    fitur_kasir.add_row(["1.", "Lihat Menu"])
    fitur_kasir.add_row(["2.", "Tambah Menu"])
    fitur_kasir.add_row(["3.", "Hapus Menu"])
    fitur_kasir.add_row(["4.", "Perbarui Menu"])
    fitur_kasir.add_row(["5.", "Halaman Utama"])
    fitur_kasir.add_row(["6.", "Keluar"])
    print(fitur_kasir)

#tabel fitur customer
def tabel_fitur_customer():
    fitur_customer = PrettyTable()
    fitur_customer.field_names = ["No.", "Fitur"]
    fitur_customer.add_row(["1.", "Pesan Menu"])
    fitur_customer.add_row(["2.", "Cek Saldo"])
    fitur_customer.add_row(["3.", "Top Up Saldo"])
    fitur_customer.add_row(["4.", "Halaman Utama"])
    fitur_customer.add_row(["5.", "Keluar"])
    print(fitur_customer)

#tabel saldo
def tabel_saldo():
    tabel_saldo = PrettyTable()
    tabel_saldo.field_names = ["No.", "Nominal"]
    tabel_saldo.add_row(["1.", "Rp10000"])
    tabel_saldo.add_row(["2.", "Rp20000"])
    tabel_saldo.add_row(["3.", "Rp50000"])
    tabel_saldo.add_row(["4.", "Rp100000"])
    tabel_saldo.add_row(["5.", "Nominal lain"])
    tabel_saldo.add_row(["6.", "Kembali"])
    print(tabel_saldo)

#tabel menu
def tabel_menu():
    tabel_menu = PrettyTable()
    with open('menu.csv', mode='r') as csv_menu:
        baca_csv_menu = csv.DictReader(csv_menu)
        tabel_menu.field_names = baca_csv_menu.fieldnames
        for row in baca_csv_menu:
            tabel_menu.add_row([row['No.'], row['Menu'], row['Harga'], row['Stok']])
    print(tabel_menu)

#register✅
def register():
    os.system("cls")
    print("\n------------------------------------------")
    print("                Register")
    print("------------------------------------------")
    try:
        try:
            with open('users.csv', mode='r', newline='') as csv_user:
                baca_csv_user = csv.DictReader(csv_user)
                data_user = list(baca_csv_user)
        except FileNotFoundError:
            with open('users.csv', mode='w', newline='') as csv_user:
                buat_csv_user = csv.writer(csv_user)
                buat_csv_user.writerow(["Nama", "Username", "Password", "Role", "Saldo"])
                data_user = [] 

        while True:
            nama = input("Masukkan nama anda: ")
            if nama.replace(" ", "").isalpha():
                break
            else:
                print("Nama harus berupa huruf, silakan coba lagi.")
                print("------------------------------------------")

        while True:
            username_sama = False
            username = input("Buat username: @").lower()
            for baris in data_user:
                if baris['Username'] == username:
                    username_sama = True
                    print("Username sudah dipakai, coba lagi yang lain!")
                    print("------------------------------------------")
                    break
            if not username_sama:
                break

        password = pwinput.pwinput("Masukkan password: ")

        while True:
            role = input("\nPilih role (kasir/customer):").lower()
            if role not in ["kasir", "customer"]:
                print("Pilihan role tidak sesuai. Silakan coba lagi.")
                print("------------------------------------------")
                time.sleep(1)
            else:
                break

        with open('users.csv', mode='a', newline='') as csv_user:
            simpan_csv_user = csv.writer(csv_user)
            simpan_csv_user.writerow([nama, username, password, role, 0])

        print(f"\nAkun @{username} berhasil ditambahkan sebagai {role}. \nSilakan login kembali.")
        time.sleep(2)
        os.system("cls")
        mulai()

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#login✅
def login():
    os.system("cls")
    print("\n------------------------------------------")
    print("                  Login")
    print("------------------------------------------")
    try:
        try:
            with open('users.csv', mode='r') as csv_user:
                baca_csv_user = csv.DictReader(csv_user)
                data_user =list(baca_csv_user)
        except FileNotFoundError:
            print("Data user belum ada, silakan register dulu")
            return

        username = input("Masukkan username: @")
        password = pwinput.pwinput("Masukkan password: ")
        role = input("Masukkan role (kasir/customer): ")

        for baris in data_user:
            if baris['Username'] == username and baris['Password'] == password and baris['Role'] == role:
                if role == "kasir":
                    print(f"\nLogin berhasil! Selamat datang, {role} @{username}")
                    time.sleep(2)
                    os.system("cls")
                    mode_kasir()
                elif role == "customer":
                    print(f"\nLogin berhasil! Selamat datang, {role} @{username}.")
                    time.sleep(2)
                    os.system("cls")
                    mode_customer(username)

        print("\nUsername/password/role salah!")
        print("------------------------------------------")

        pilihan_ulang = input("\nCoba lagi? (kembali/login): ").lower()
        if pilihan_ulang == "kembali":
            os.system("cls")
            mulai()
        elif pilihan_ulang == "login":
            os.system("cls")
            login()
        else:
            print("Pilihan tidak sesuai. Silakan coba lagi.")
            time.sleep(1)
            return

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#logout✅
def logout():
    print("\n--- Terima kasih atas kunjungan Anda! ---")
    sys.exit()

#mode kasir✅
def mode_kasir():
    try:
        while True:
            print("\n------------------------------------------")
            print("              Mode: Kasir")
            print("------------------------------------------")
            tabel_fitur_kasir()
            pilih_fitur = input("\nPilih fitur (1/2/3/4/5/6): ")
            if pilih_fitur == "1":
                os.system("cls")
                lihat_menu()
            elif pilih_fitur == "2":
                os.system("cls")
                tambah_menu()
            elif pilih_fitur == "3":
                os.system("cls")
                hapus_menu()
            elif pilih_fitur == "4":
                os.system("cls")
                fitur_perbarui_menu()
            elif pilih_fitur == "5":
                os.system("cls")
                mulai()
            elif pilih_fitur == "6":
                logout()
            else:
                print("Pilihan tidak sesuai, silakan coba lagi.")
                time.sleep(1.5)
                os.system("cls")
                continue

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#mode customer✅
def mode_customer(username):
    try:
        while True:
            print("\n------------------------------------------")
            print("             Mode: Customer")
            print("------------------------------------------")
            tabel_fitur_customer()
            pilih_fitur = input("\nPilih fitur (1/2/3/4/5): ")
            if pilih_fitur == "1":
                os.system("cls")
                pesan_menu(username)
            elif pilih_fitur == "2":
                cek_saldo(username)
            elif pilih_fitur == "3":
                os.system("cls")
                top_up(username)
            elif pilih_fitur == "4":
                os.system("cls")
                mulai()
            elif pilih_fitur == "5":
                logout()
            else:
                print("Pilihan tidak sesuai, silakan coba lagi.")
                time.sleep(1.5)
                os.system("cls")
                continue

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#fitur lihat menu✅
def lihat_menu():
    print("============== KOFISYOP MENU =============")
    tabel_menu()

#fitur pesan menu✅
def pesan_menu(username):
    print("------------------------------------------")
    print("               Pesan Menu")
    print("------------------------------------------")
    tabel_menu()
    while True:
        try:
            try:
                pilih_menu = int(input("Pilih nomor menu: "))
                try:
                    with open('menu.csv', mode='r') as csv_menu:
                        baca_csv_menu = csv.DictReader(csv_menu)
                        data_menu =list(baca_csv_menu)
                except FileNotFoundError:
                    print("Data menu tidak ada")
                    return

                menu_ada = None
                for baris in data_menu:
                    if baris['No.'] == str(pilih_menu):
                        menu_ada = baris
                        break
                if menu_ada:
                    try:
                        harga_menu = int(menu_ada['Harga'])
                        stok_awal = int(menu_ada['Stok'])
                        while True:
                            try:
                                jumlah_pesanan = int(input("Jumlah pesanan: "))
                                break
                            except ValueError:
                                print("Jumlah harus berupa angka, silakan coba lagi.")
                                print("------------------------------------------")
                                continue
                        if stok_awal <= 0:
                            print(f"Stok menu {menu_ada['Menu']} habis. Silakan pilih menu lain.")
                            print("------------------------------------------")
                            continue
                        if jumlah_pesanan > stok_awal:
                            print(f"Stok tidak cukup. Menu {menu_ada['Menu']} hanya tersisa {stok_awal} stok.")
                            print("------------------------------------------")
                            continue

                        total_harga = harga_menu *jumlah_pesanan 

                        with open('users.csv', mode='r') as csv_user:
                            baca_csv_user = csv.DictReader(csv_user)
                            data_user = list(baca_csv_user)

                        user_ada = None
                        for baris in data_user:
                            if baris['Username'] == username:
                                user_ada = baris
                                break
                        if user_ada:
                            saldo_user = int(user_ada['Saldo'])
                            if saldo_user >= total_harga:
                                sisa_saldo = saldo_user - total_harga
                                user_ada['Saldo'] = str(sisa_saldo)

                                print("Pesanan akan segera diproses...")
                                time.sleep(2)

                                with open('users.csv', mode='w', newline='') as csv_user:
                                    tulis_csv_user = csv.writer(csv_user)
                                    tulis_csv_user.writerow(["Nama", "Username", "Password", "Role", "Saldo"])
                                    for item in data_user:
                                        tulis_csv_user.writerow([item['Nama'], item['Username'], item['Password'], item['Role'], item['Saldo']])

                                stok_awal = int(menu_ada['Stok'])
                                sisa_stok = stok_awal - jumlah_pesanan
                                menu_ada['Stok'] = str(sisa_stok)

                                with open('menu.csv', mode='w', newline='') as csv_menu:
                                    tulis_csv_menu = csv.writer(csv_menu)
                                    tulis_csv_menu.writerow(["No.", "Menu", "Harga", "Stok"])
                                    for item in data_menu:
                                        tulis_csv_menu.writerow([item['No.'], item['Menu'], item['Harga'], item['Stok']])
                                
                                os.system("cls")
                                print("\n=================================================")
                                print("                K O F I S Y O P")
                                print("=================================================")
                                print(f"Tanggal          : {datetime.now()}")
                                print(f"Customer         : {user_ada['Nama']}")
                                print(f"Pesanan          : {menu_ada['Menu']}")
                                print(f"Jumlah Pesanan   : {jumlah_pesanan}")
                                print("=================================================")
                                print(f"Total Harga      : Rp{total_harga}")
                                print(f"Sisa Saldo       : Rp{sisa_saldo}")
                                print("=================================================")
                                print("       #TERIMA KASIH ATAS KUNJUNGAN ANDA")
                                print("=================================================")
                                
                                while True:
                                    pilihan_lanjut = input("\nApakah ingin memesan lagi? (y/t): ").lower()
                                    if pilihan_lanjut == "y":
                                        os.system("cls")
                                        pesan_menu(username)
                                    elif pilihan_lanjut == "t":
                                        os.system("cls")
                                        mode_customer(username)
                                    else:
                                        print("------------------------------------------")
                                        print("Pilihan tidak sesuai, silakan coba lagi.")
                                        time.sleep(1)
                                        continue
                            else:
                                print("Saldo anda tidak cukup. \nSilakan top up terlebih dahulu.")
                                print("------------------------------------------")
                                while True:
                                    pilihan_lanjut = input("\nApakah ingin top up? (y/t): ").lower()
                                    if pilihan_lanjut == "y":
                                        os.system("cls")
                                        top_up(username)
                                    elif pilihan_lanjut == "t":
                                        os.system("cls")
                                        mode_customer(username)
                                    else:
                                        print("------------------------------------------")
                                        print("Pilihan tidak sesuai, silakan coba lagi.")
                                        time.sleep(1)
                                        continue
                        else:
                            print("User tidak ditemukan.")
                            print("------------------------------------------")
                            return
                    except ValueError:
                        print("Terjadi kesalahan, silakan coba lagi.")
                        print("------------------------------------------")
                        return
                else:
                    print("Menu tidak ada, silakan coba lagi.")
                    print("------------------------------------------")
                    continue
            except ValueError:
                    print("Nomor harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue
        except KeyboardInterrupt:
            print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
            time.sleep(2)
            logout()
        except EOFError:
            print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
            time.sleep(2)
            logout()

#fitur tambah menu✅
def tambah_menu():
    print("------------------------------------------")
    print("               Tambah Menu")
    print("------------------------------------------")
    lihat_menu()
    try:
        try:
            with open('menu.csv', mode='r') as csv_menu:
                baca_csv_menu = csv.DictReader(csv_menu)
                data_menu =list(baca_csv_menu)

            while True:
                try:
                    no_menu = int(input("Masukkan nomor menu baru: "))
                    menu_ada = False
                    for baris in data_menu:
                        if baris['No.'] == str(no_menu):
                            menu_ada = True
                            print(f"Menu nomor {no_menu} sudah ada, silakan coba lagi.")
                            print("------------------------------------------")
                            break
                    if menu_ada:
                        continue

                    while True:
                        menu_baru = input("Nama menu baru: ")
                        if menu_baru.replace(" ", "").isalpha():
                            break
                        else:
                            print("Menu harus berupa huruf, silakan coba lagi.")
                            print("------------------------------------------")
                    break

                except ValueError:
                    print("Nomor harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue

            while True:
                try:
                    harga_baru = int(input("Harga menu baru: "))
                    break
                except ValueError:
                    print("Harga harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue

            while True:
                try:
                    stok_baru = int(input("Banyak stok: "))
                    break
                except ValueError: 
                    print("Stok harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue

            with open('menu.csv', mode='a', newline='') as csv_menu:
                writer = csv.writer(csv_menu)
                writer.writerow([no_menu, menu_baru, harga_baru, stok_baru])

            print(f"menu baru '{[menu_baru]}' berhasil ditambahkan")
            time.sleep(2)
            os.system("cls")
            mode_kasir()

        except FileNotFoundError:
            print("Data menu tidak ditemukan")
            return

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#fitur hapus menu✅
def hapus_menu():
    print("------------------------------------------")
    print("               Hapus Menu")
    print("------------------------------------------")
    lihat_menu()
    try:
        try:
            with open('menu.csv', mode='r') as csv_menu:
                baca_csv_menu = csv.DictReader(csv_menu)
                data_menu =list(baca_csv_menu)

            while True:
                try:
                    no_menu = int(input("Pilih nomor menu yg ingin dihapus: "))
                    menu_ada = False
                    for nomor in data_menu:
                        if nomor['No.'] == str(no_menu):
                            data_menu.remove(nomor)
                            menu_ada = True
                            break
                    if menu_ada:
                        with open('menu.csv', mode='w', newline='') as csv_menu:
                            tulis_csv_menu = csv.writer(csv_menu)
                            tulis_csv_menu.writerow(["No.", "Menu", "Harga", "Stok"])
                            for item in data_menu:
                                tulis_csv_menu.writerow([item['No.'], item['Menu'], item['Harga'], item['Stok']])

                        print("------------------------------------------")
                        print(f"Menu nomor {no_menu} berhasil dihapus.")

                        pilihan_ulang = input("\nHapus menu lagi? (y/t): ").lower()
                        if pilihan_ulang == "y":
                            os.system("cls")
                            hapus_menu()
                        elif pilihan_ulang == "t":
                            os.system("cls")
                            mode_kasir()
                        else:
                            print("Pilihan tidak sesuai, silakan coba lagi.")
                            time.sleep(1)
                            return

                    else:
                        print(f"Menu nomor {no_menu} tidak ada.") 
                        print("------------------------------------------")
                except ValueError:
                    print("Nomor harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue
        except FileNotFoundError:
            print("Data menu tidak ditemukan.")

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#fitur ubah menu✅
def fitur_perbarui_menu():
    print("------------------------------------------")
    print("               Update Menu")
    print("------------------------------------------")
    lihat_menu()
    try:
        try:
            with open('menu.csv', mode='r') as csv_menu:
                baca_csv_menu = csv.DictReader(csv_menu)
                data_menu =list(baca_csv_menu)

            while True:
                try:
                    no_menu = int(input("Pilih nomor menu yang ingin diubah: "))
                    menu_ada = False
                    for baris in data_menu:
                        if baris['No.'] == str(no_menu):
                            menu_ada = True

                            pilihan_ubah = input("\nMau ubah apa? (menu/harga/stok): ").lower()
                            print("------------------------------------------")

                            if pilihan_ubah == "menu":
                                while True:
                                    try:
                                        perubahan = input("Tulis nama menu yang baru: ")
                                        baris['Menu'] = perubahan
                                    except ValueError:
                                        print("Menu harus berupa huruf, silakan coba lagi.")
                                        print("--------------------------------------------")
                                        continue
                            elif pilihan_ubah == "harga":
                                while True:
                                    try:
                                        baris['Harga'] = int(input("Masukkan harga terbaru: "))
                                        break
                                    except ValueError:
                                        print("Harga harus berupa angka, silakan coba lagi.")
                                        print("--------------------------------------------")
                                        continue
                            elif pilihan_ubah == "stok":
                                while True:
                                    try:
                                        baris['Stok'] = int(input("masukkan stok terbaru: "))
                                        break
                                    except ValueError:
                                        print("stok harus berupa angka, silakan coba lagi.")
                                        print("--------------------------------------------")
                                        continue
                            else:
                                print("Pilihan tidak sesuai, silakan coba lagi.")
                                time.sleep(1)
                                continue

                    if not menu_ada:
                        print("Menu tidak ditemukan, silakan coba lagi.")
                        print("----------------------------------------")
                        continue

                    with open('menu.csv', mode='w', newline='') as csv_menu:
                        tulis_csv_menu = csv.writer(csv_menu)
                        tulis_csv_menu.writerow(["No.", "Menu", "Harga", "Stok"])
                        for item in data_menu:
                            tulis_csv_menu.writerow([item['No.'], item['Menu'], item['Harga'], item['Stok']])
                    
                    print("--------------------------------------------")
                    print(f"Menu pada nomor {no_menu} berhasil diperbarui.")

                    while True:     
                        pilihan_ulang = input("\nUbah menu lagi? (ya/tidak): ").lower()
                        if pilihan_ulang == "ya":
                            os.system("cls")
                            fitur_perbarui_menu()
                        elif pilihan_ulang == "tidak":
                            os.system("cls")
                            mode_kasir()
                        else:
                            print("Pilihan tidak sesuai, silakan coba lagi.")
                            continue

                except ValueError:
                    print("Nomor harus berupa angka, silakan coba lagi.")
                    print("------------------------------------------")
                    continue

        except FileNotFoundError:
            print("Data menu tidak ada")
            return

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#fitur cek saldo✅
def cek_saldo(username):
    print("\n------------------------------------------")
    print("                 Saldo")
    print("------------------------------------------")
    try:
        try:
            with open('users.csv', mode='r') as csv_user:
                baca_csv_user = csv.DictReader(csv_user)
                data_user =list(baca_csv_user)
        except FileNotFoundError:
            print("Data user tidak ditemukan")
            return

        username_ada = False
        for baris in data_user:
            if baris["Username"] == username:
                username_ada = True
                print(f"Saldo anda: Rp{baris['Saldo']}")

                while True:
                    pilihan_lanjut = input("\nApakah ingin top up saldo? (y/t): ").lower()
                    if pilihan_lanjut == "y":
                        os.system("cls")
                        top_up(username)
                    elif pilihan_lanjut == "t":
                        os.system("cls")
                        mode_customer(username)
                    else:
                        print("------------------------------------------")
                        print("Pilihan tidak sesuai, silakan coba lagi.")
                        time.sleep(1)
                        continue

        if not username_ada:
            print("Username tidak ditemukan")

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#fitur top up saldo✅
def top_up(username):
    print("\n------------------------------------------")
    print("              Top Up Saldo")
    print("------------------------------------------")
    tabel_saldo()
    try:
        try:
            with open('users.csv', mode='r') as csv_user:
                baca_csv_user = csv.DictReader(csv_user)
                data_user =list(baca_csv_user)
        except FileNotFoundError:
            print("Data user belum ada, silakan register dulu")
            return
        
        user_ada = None
        for baris in data_user:
            if baris['Username'] == username:
                user_ada = baris
                break
        if not user_ada:
            print("user tidak ada.")
            return

        while True:
            pilihan = input("Masukkan pilihan Anda (1/2/3/4/5/6): ")
            if pilihan == '1':
                nominal_topup = 10000
            elif pilihan == '2':
                nominal_topup = 20000
            elif pilihan == '3':
                nominal_topup = 50000
            elif pilihan == '4':
                nominal_topup = 100000
            elif pilihan == '5':
                while True:
                    try:
                        nominal_topup = int(input("Masukkan nominal top up: Rp"))
                        if nominal_topup <= 0:
                            print("Nominal tidak boleh Rp0. Silakan coba lagi.")
                            print("------------------------------------------")
                            continue
                        break
                    except ValueError:
                        print("Nomor harus berupa angka, silakan coba lagi.")
                        print("------------------------------------------")
                        continue
            elif pilihan == '6':
                os.system("cls")
                mode_customer(username)
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                print("------------------------------------------")
                continue

            saldo_awal = int(user_ada['Saldo'])
            saldo_baru = saldo_awal + nominal_topup
            user_ada['Saldo'] = str(saldo_baru)

            try:
                with open('users.csv', mode='w', newline='') as csv_user:
                    tulis_csv_user = csv.writer(csv_user)
                    tulis_csv_user.writerow(["Nama", "Username", "Password", "Role", "Saldo"])
                    for item in data_user:
                        tulis_csv_user.writerow([item['Nama'], item['Username'], item['Password'], item['Role'], item['Saldo']])
                print("------------------------------------------")
                print(f"Saldo berhasil ditambahkan sebesar Rp {nominal_topup}. \nSaldo anda saat ini: Rp {user_ada['Saldo']}")

                while True:
                    pilihan_lanjut = input("\nApakah ingin top up lagi? (y/t): ").lower()
                    if pilihan_lanjut == "y":
                        os.system("cls")
                        top_up(username)
                    elif pilihan_lanjut == "t":
                        os.system("cls")
                        mode_customer(username)
                    else:
                        print("------------------------------------------")
                        print("Pilihan tidak sesuai, silakan coba lagi.")
                        time.sleep(1)
                        continue

            except ValueError:
                print("Data tidak berhasil disimpan")

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

#mulai✅
def mulai():
    try:
        while True:
            print("\n============== Menu Utama ================")
            tabel_menu_utama()
            pilih = input("Pilih fitur (1/2/3): ")
            if pilih == "1":
                register()
            elif pilih == "2":
                login()
            elif pilih == "3":
                logout()
            else:
                print("\nPilihan tidak sesuai. Silakan coba lagi.")
                time.sleep(1)
                os.system("cls")
                continue

    except KeyboardInterrupt:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()
    except EOFError:
        print("Permintaan tidak dapat diproses. Anda akan keluar dari program... ")
        time.sleep(2)
        logout()

mulai()