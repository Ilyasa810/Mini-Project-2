from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["NAMA", "NIM", "KELAS",]
table.add_row(["Muhammad Ilyasa' 'Izzuddin", 2409116033, "Kelas A' 2024"])
print(table)

table = PrettyTable()
table.field_names = ["No Film", "Judul Film", "Penilaian", "Ulasan"]

katalog_film = []


def film(No, Judul_film):
    table.add_row([No, Judul_film, [], []])

film('1', 'Deadpool & Wolverine ')
film('2', 'Transformers: One ')
film('3', 'Godzilla X Kong: The New Empire ')
film('4', 'Madame Web')
film('5', 'Aquaman: The Lost Kingdom')
film('6', "Five Nights at Freddy's")
film('7', 'The Marvels')

def tampil_pesan_selamat_datang():
    print("=" * 50)
    print("🎬🎥 << Selamat Datang di Cinema Catalogue kami! >> 🎥🎬")
    print("=" * 50)

def menu_login():
    print("1. Admin")
    print("2. Pengguna")
    print("=" * 50)

def tampilan_menu_admin():
    print("\n<<Selamat Datang Admin!!>>")
    print("1. Tambah Film")
    print("2. Hapus Film")
    print("3. Lihat Film")
    print("4. Kembali ke Mode Login")
    print("5. Keluar")

def login(): #definiton untuk login
    while True:
        tampil_pesan_selamat_datang()
        menu_login()
        pilihan = input("\nSilahkan memilih role anda: ") #memilih role
        if pilihan  == "1": # jika memilih nomor 1 
            admin() #maka, akan menjadi admin
        elif pilihan == "2": # jika memilih nomor 2
            pengguna() # akan menjadi pengguna
        else:
            print("Tidak ada role yang anda pilih, silakan coba kembali nanti.") 
            exit() # jika tidak memilih role akan langsung keluar

def admin(): #definiton untuk admin
    print("\n<<Anda Admin? Silahkan Masukkan Password terlebih dahulu>>: ")
    password = input("\nMasukkan password admin: ") # masukkan password admin
    pass_admin = '123'
    if password == pass_admin: # jika password sama dengan password yang benar
        admin2()  # maka langsung ke tahap berikutnya
    else: # jika memasukkan password yang salah
        print(" \n[Sepertinya, kita terjebak di Universe yang salah. Mari kembali.] ") 
        admin()  # maka, akan diminta untuk memasukkan password admin kembali
        return None


def admin2():
    while True:    
        tampilan_menu_admin()
        fitur = input("Silahkan memilih fitur yang diinginkan: ") # memilih fitur yang ingin dipilih sebagai admin
        if fitur == "1": # jika memilih nomor 1
            tambah_film() # langsung diarahkan ke menambahkan film
        elif fitur == "2": # jika memilih nomor 2
            hapus_film() # Langsung diarahkan ke menghapus film
        elif fitur == "3": # jika memilih nomor 3
            lihat_film_yang_sudah_ada() # Langsung diarahkan untuk melihat table film yang sudah tersedia
        elif fitur == "4": # jika memilih nomor 4
            login() # Langsung diarahkan kembali ke login
        elif fitur == "5": # jika memilih nomor 5
            print("Sampai Jumpa dilain kesempatan, Keep Exploring The Multiverse!")
            exit() # langsung keluar dari program
        else: # Jika tidak ada yang dipilih maka akan kembali ke pemilihan role.
            print("Oops, tidak ada fitur yang dipilih. ") 
            break

def tambah_film():
    while True:
        lihat_film_yang_sudah_ada()
        no_film = input("Masukkan Nomor Film: ") #masukkan nomor film/urutan nomor film yang ingin ditambahkan
        judul_film = input("Masukkan Judul Film: ") # Masukkan judul film yang ingin ditambahkan
        film(no_film, judul_film)
        print(f"\nSelamat!! Nomor Film ke-{no_film} dengan judul {judul_film} berhasil ditambahkan.")
        lihat_film_yang_sudah_ada()

# diberi pilihan apakah ingin melanjutakannya
        pilihan = input("Apakah anda ingin menambahkan film lagi? (ya/tidak): ") 
        if pilihan == "tidak": # jika tidak maka akan kembali ke pemilihan fitur
            break

def hapus_film():
    while True:
        lihat_film_yang_sudah_ada() #akan diperlihatkan terlebih dahulu tabelnya
        no_film = input("Masukkan Nomor Film yang ingin dihapus: ") # memasukkan nomor urutan film yang ingin dihapus

        # Mencari dan menghapus film dari table
        for row in table._rows:
            if row[0] == no_film:
                table.del_row(table.rows.index(row))
                print(f"Nomor film ke-{no_film} telah terhapus. ")
                lihat_film_yang_sudah_ada()
                break
        else: 
            print("Nomor film tidak ditemukan.")

# diberi pilihan apakah ingin melanjutkannya lagi?
        pilihan = input("Apakah ada film yang ingin dihapus lagi? (ya/tidak): ")
        if pilihan == "tidak":
            break

def lihat_film_yang_sudah_ada(): # jika hanya ingin melihat table film
    print("\n🎬Berikut adalah Katalog Film yang tersedia🎬: ")
    print(table)

def pengguna():
    nama_pengguna = input("Masukkan Nama Anda: ") # masukkan nama pengguna
    print("Selamat datang", nama_pengguna)

    password = input("Masukkan password pengguna: ") # masukkan password pengguna
    pass_pengguna = '0000'
    if password == pass_pengguna: # jika password sama dengan password yang benar
        pengguna2()  # maka langsung ke tahap berikutnya
    else:
        print("Cobalah lagi") # jika tak sesuai 
        pengguna()  # akan mengulang kembali ke masukkan nama pengguna dan seterusnya
        return None

def pengguna2():
    while True:
        lihat_film_yang_sudah_ada() # diperlihatkan terlebih dahulu table filmnya
        no_film = input("Masukkan Urutan Nomor Film yang ingin Anda beri ulasan dan penilaian: ")
        #masukkan nomor urut dari filmnya

        for row in table._rows:
            if row[0] == no_film:
                ulasan = str(input("Masukkan Ulasan Anda: ")) #memasukkan ulasan
                while True:
                    try:
                        penilaian = float(input("Masukkan Penilaian Anda (1-10): "))
                        if penilaian < 1 or penilaian > 10: # jika tidak diantara 1-10, maka akan error dan mengulang
                            print("Error: Penilaian harus dalam rentang 1-10.")
                        else:
                            break  # penilaian sesuai ketentuan, akan lanjut ke tahap berikutnya
                    except ValueError:
                        print("Error: Masukkan nilai yang valid untuk penilaian.")

                row[2].append(penilaian) # penilaian di kolom 2
                row[3].append(ulasan) # ulasan di kolom 3

                print(f"\nSelamat!! Ulasan dan penilaian untuk film '{row[1]}' berhasil ditambahkan.")
                break
        else: # jika tidak ada di daftar/table maka akan gagal
            print("Nomor film tidak dapat ditemukan, silahkan coba lagi.")

# diminta apakah ingin melanjutkan atau tidak
        pilihan = input("Apakah anda ingin memberikan ulasan untuk film lain? (ya/tidak): ")
        if pilihan == "tidak": # jika tidak maka, akan ditampilkan table yang sudah diberi penilaian dan ulasan tadi
            lihat_film_yang_sudah_ada()
            print("||Thank You and Keep Exploring The Multiverse!!||")
            exit()
            break

# Memulai program
if __name__ == "__main__":
    login()
