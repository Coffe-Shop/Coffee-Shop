# `˗ˏˋ☕ˎˊ˗ k o f i s y o p ˗ˏˋ☕ˎˊ˗
Laporan Praktikum Proyek Akhir Mata Kuliah Dasar-Dasar Pemrograman

### Kelompok 2 | Sistem Informasi A | Tema: Coffee-Shop
1. Adella Putri (2409116006)
2. Dilla Maharani (2409116023)
3. Sayid Rafi A'thaya (2409116036)

# ⤷ Flowchart
![Flowchart Kelompok Coffe Shop-Halaman-1 (1)](https://github.com/user-attachments/assets/c29f6c51-db97-49fd-9866-0b4c2089d401)

# ⤷ Penjelasan Output 

## A. Tampilan Menu Utama Program
![Screenshot 2024-11-09 081916](https://github.com/user-attachments/assets/ac5a7ed2-034e-4529-84ee-642ff8d8765e)

Saat pertama kali program dijalankan, pengguna akan melihat pesan selamat datang, beserta dengan tabel menu utama yaang berupa Registrasi, Login, dan Logout.


### 1. Menu Registrasi

Jika pengguna memilih pilihan menu utama (nomor 1) maka sistem akan beralih ke bagian proses registrasi
![Screenshot 2024-11-09 082309](https://github.com/user-attachments/assets/2d6719df-fac4-4a18-b93f-259926e9993d)
![Screenshot 2024-11-09 083913](https://github.com/user-attachments/assets/96730ad8-f4c0-4b24-9852-933e1693425c)

Menu registrasi ini digunakan apabila pengguna belum memiliki akun atau belum pernah mendaftarkan akun nya didalam sistem,
jika pengguna belum memiliki akun, maka disarankan untuk pengguna registrasi terlebih dahulu dengan mengisi :
- nama
- username
- password
- dan juga memilih role (apa pengguna mendaftar sebagai kasir atau customer)
  
### 2. Menu Login

Setelah pengguna telah berhasil mendaftarkan akun nya kedalam sistem, maka pengguna akan diarahkan kembali ke halaman utama, 
yaitu bagiam Login.

![Screenshot 2024-11-09 082818](https://github.com/user-attachments/assets/1c47cc61-4ec6-4e59-9e6a-ea27cd9b747b)
![Screenshot 2024-11-09 083939](https://github.com/user-attachments/assets/fa731507-47f8-4b3b-b419-3b940eb53dc0)

Di menu Login ini, pengguna akan kembali memasukkan Username, Password, dan juga pilihan role yang telah didaftarkan sebelumnya.

### 2. Menu Logout

![Screenshot 2024-11-09 110450](https://github.com/user-attachments/assets/e135afbe-3200-4005-909b-5100522c476c)

Jika pengguna telah selesai menggunakan sistem, pengguna bisa memilih untuk mengakhirir sistem dengan cara memilih menu utama Logout. 
Maka pengguna akan otomatis keluar dari sistem.

## B. Tampilan Menu Kasir

Jika pengguna telah selesai melakukan Login pada sistem, dan pengguna memilih role Kasir, 

berikut merupakan Menu Tampilan fitur-fitur apa saja yang dapat di lakukan kasir di dalam sistem.

![Screenshot 2024-11-09 082923](https://github.com/user-attachments/assets/4e0cf65a-0d42-4e39-a10a-18ee028b9dc8)

terdapat 6 Menu pilihan utama yang dapat dipilih, dengan hanya tinggal memasukkan nomor yang tertera pada tabel Menu kasir, 
maka pengguna akan secara otomatis tertampil menu-menu pilihan fitur yang mereka inginkan.

### 1. Fitur Lihat Menu

Jika pengguna memilih Fitur Lihat menu :

![Screenshot 2024-11-09 083035](https://github.com/user-attachments/assets/c6eda575-c416-4978-9bee-2835a92ae192)

Maka pengguna akan ditampilkan List Menu yang dijual atau tersedia di dalam Coffe Shop,
berupa keterangan :
- Nomor
- Nama
- Harga
- dan, Stok

Setelah itu, pengguna akan dialihkan kembali kedalam Tampilan Menu Utama Kasir, dan kasir dapat memilih kembali pilihan ingin berinteraksi dengan fitur pilihan yang mana. 

### 2. Fitur Tambah Menu

Jika pengguna memilih Fitur Tambah Menu :

![Screenshot 2024-11-09 083128](https://github.com/user-attachments/assets/540b6a4c-ddb9-43f6-adcb-08505708d3f7)

Maka pengguna akan diberikan kembali tabel list menu Coffe Shop, lalu pengguna perlu untuk memasukkan beberapa hal dibawah ini, untuk dapat menambahkan menu baru. Berupa :
- memasukkan nomor menu baru yang ingin di tambahkan,
- memasukkan nama menu baru
- harga menu baru
- banyak stok pada menu tersebut

Dan, jika penggguna telah selesai dan berhsil memasukkan beberapa hal tersebut, maka setelah itu menu baru akan tertambah pada sistem didalam file penyimpanan CSV.
dan pengguna dapat melihat menu baru yang telah ditambahkan didalam daftar list menu yang berada pada Fitur 1(Lihat Menu)

### 3. Fitur Hapus Menu

Jika pengguna memilih Fitur Hapus Menu :

![Screenshot 2024-11-09 083304](https://github.com/user-attachments/assets/1dd1c73a-dc47-48da-8ad9-b2587b32ba4b)

Maka pengguna hanya perlu untuk memasukkan Nomor menu pada tabel untuk dapat di hapus, secara otomatis menu yang terdapat pada nomor yang di masukkan pengguna akan terhapus.

### 4. Fitur Perbarui Menu

Jika pengguna memilih Fitur Perbarui Menu :

![Screenshot 2024-11-09 083528](https://github.com/user-attachments/assets/347e4922-98ac-4516-9d63-50002d39a3f8)

Untuk memperbarui menu, pengguna terlebih dahulu perlu untuk :
- memasukkan nomor menu baru,
- memasukkan nama menu baru
- dan banyak nya stok pada menu yang ingin diperbarui
Maka setelah itu, menu yang terlah di perbarui akan ditambahkan kembali kedalam sistem.

### 5. Halaman Utama

Jika pengguna memilih Fitur Halaman Utama :

![Screenshot 2024-11-09 081916](https://github.com/user-attachments/assets/11766f84-f2f2-44b9-a8a4-e90ecc5f65db)

Maka pengguna otomatis akan diarahkan kembali ke menu utama bagian Register, Login, dan Logout.

### 6. Keluar

Dan jika pengguna memilih fitur keluar :

![Screenshot 2024-11-09 083654](https://github.com/user-attachments/assets/7c46453a-1eb1-44f1-902f-689b1cb11877)

Maka pengguna akan secara otomatis keluar dari sistem.

# C. Tampilan Menu Customer
![Screenshot 2024-11-09 084002](https://github.com/user-attachments/assets/31d50bf8-4e75-4fea-9dd5-a9ef07a6bd78)

### 1. Fitur Pesan Menu
![Screenshot 2024-11-09 084659](https://github.com/user-attachments/assets/0679d8f8-035e-4281-a6d2-c246800d7122)
![Screenshot 2024-11-09 084725](https://github.com/user-attachments/assets/4dec0d31-c588-4e03-88aa-a51c0724b187)

(beri penjelasan disini)
### 2. Fitur Cek Saldo
![Screenshot 2024-11-09 084433](https://github.com/user-attachments/assets/5196337a-dee4-4275-8429-1c0f425a2cf9)

(beri penjelasan disini)
### 3. Fitur Top Up Saldo
![Screenshot 2024-11-09 084529](https://github.com/user-attachments/assets/9fdb0030-8e88-4d10-b8b3-f1c66ac2fde7)

(beri penjelasan disini)
### 4. Halaman Utama
![Screenshot 2024-11-09 081916](https://github.com/user-attachments/assets/ff1e21aa-6b88-4489-ba97-c8f7de8978de)

(beri penjelasan disini)
### 5. Keluar
![Screenshot 2024-11-09 084755](https://github.com/user-attachments/assets/57ab66c2-7cbb-462f-8fbe-8c9e62a223e2)

(beri penjelasan disini)

