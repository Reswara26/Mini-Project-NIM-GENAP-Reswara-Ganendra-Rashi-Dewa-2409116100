# Input Nama dan NIM
print("\n=========== LAKUKAN LOGIN TERLEBIH DAHULU ==========")
nama_benar = "RESWARA GANENDRA RASHI DEWA"
nim_benar = 2409116100
print("Silakan Isi Nama dan NIM Anda Terlebih Dahulu!")
login = True
while (login==True):
    nama = str(input("Masukkan Nama Anda: "))
    nim = int(input("Masukkan NIM Anda: "))
    if nama_benar == nama and nim_benar == nim:
        login = False
        print(f"Login Berhasil! Selamat Datang {nama}!")

        # Input Harga Barang dan Jumlah Barang
        harga = True
        while (harga==True):
            print("\n=========== MENGHITUNG TOTAL HARGA BARANG ===========")
            print("Silakan Isi Harga Barang dan Jumlah Barang")
            harga_barang = float(input("Masukkan Harga Barang yang Dibeli: Rp. "))
            jumlah_barang = int(input("Masukkan Jumlah Barang yang Dibeli: "))
            total_harga = harga_barang * jumlah_barang
            if total_harga > 250000:
                diskon = total_harga * 0.25
                total_harga -= diskon
                print("\nSelamat! Anda Mendapatkan Diskon Sebesar 25%!")
                print(f"Total Harga Barang Anda Setelah Diskon Menjadi: Rp. {total_harga:.2f}")
                yt = True
                while (yt==True):
                    y = str(input("\nIngin Menghitung Kembali Total Harga? (Ya/Tidak): "))
                    if y == "Ya":
                        yt = False
                        harga = True
                    elif y == "Tidak":
                        yt = False
                        harga = False
                        print("\nTerima Kasih Telah Berbelanja, Silakan Datang Kembali!")
                    else:
                        yt = True
                        print("*!* Input Tidak Sesuai *!*")
            else:
                print(f"\nTotal Harga Barang Anda Sebesar: Rp. {total_harga:.2f}")
                yt = True
                while (yt==True):
                    y = str(input("\nIngin Menghitung Kembali Total Harga? (Ya/Tidak): "))
                    if y == "Ya":
                        yt = False
                        harga = True
                    elif y == "Tidak":
                        yt = False
                        harga = False
                        print("\nTerima Kasih Telah Berbelanja, Silakan Datang Kembali!")
                    else:
                        yt = True
                        print("*!* Input Tidak Sesuai *!*")

    else:
        print("*!* Nama atau NIM Salah, Silakan Coba Lagi *!*")
        login = True