print("================================================================================")
print("======== Aplikasi Pengumpulan Nilai Mata Kuliah Sistem Informasi ===============")
print("================================================================================")
print ("Nama          : Mikhel febian")
print ("NIM           : 2509116056")
print ("Program Studi : Mikhel Sistem Informasi")
print ("Mata Kuliah   : Dasar - Dasar Pemrograman")
print ("Program       : Sistem Pengumpulan Data Dengan mengimplementasikan Create, Read, dan Update.")

daftar_mahasiswa_si = [] # list Kosong untuk menampung data mahasiswa
mata_kuliah = [] # list kosong untuk menampung mata kuliah


while True: # perulangan tanpa henti
    print("\nMenu Utama") # Menampilkan menu utama
    print("1. Tambah Data Mahasiswa")
    print("2. Tambah Mata Kuliah dan Nilai Mahasiswa")
    print("3. Tampilkan Data Mahasiswa dan Mata Kuliah")
    print("4. Keluar")
    
    opsi_menu = input("Opsi Pilihan : ") # opsi pilihan menu utama
    
    if opsi_menu == "1": # Menambahkan data mahasiswa
        nama = input("Masukkan Nama : ")
        nim = input("Masukkan NIM : ")
        angkatan = input("Masukkan Angkatan : ")
        daftar_mahasiswa_si.append([nama, nim, angkatan, []])
        print("Data mahasiswa berhasil ditambahkan.")

    elif opsi_menu == "2": # Menambahkan mata kuliah dan nilai mahasiswa
        if not daftar_mahasiswa_si: 
            print("Belum ada Mahasiswa. ")
        else:
            print("\nPilih Mahasiswa")
            for mahas in daftar_mahasiswa_si :# Menampilkan daftar mahasiswa
                print(f"{mahas[0]} {mahas[1]}")
                pilih = int(input("Masukkan urutan mahasiswa: ")) - 1
                if 0 <= pilih < len(daftar_mahasiswa_si):
                    matkul = input("Masukkan Nama Mata Kuliah : ")
                    nilai = input("Masukkan Nilai Mata Kuliah : ")
                    daftar_mahasiswa_si[pilih][3].append([matkul, nilai]) # Menambahkan mata kuliah dan nilai ke mahasiswa yang dipilih
                    print("Mata kuliah dan nilai berhasil ditambahkan.")
                else:
                    print("Pilihan tidak ada.")

    elif opsi_menu == "3": # Menampilkan data mahasiswa dan mata kuliah
        if not daftar_mahasiswa_si:
            print("Belum ada data mahasiswa.")
        else:
            print("\nData Mahasiswa dan Mata Kuliah")
            for mahas in daftar_mahasiswa_si:
                print(f"\nNama: {mahas[0]}, NIM: {mahas[1]}, Angkatan: {mahas[2]}") # menampilkan data mahasiswa
                if not mahas[3]:
                    print("   Belum ada mata kuliah.")
                else:
                    for makul in mahas[3]:
                        print(f"- {makul[0]} : Nilai: {makul[1]}") #menampilkan nama mata kuliah dan nilai

    elif opsi_menu == "4": # Keluar dari program
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak ada.")
