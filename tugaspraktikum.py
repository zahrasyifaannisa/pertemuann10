# data dict kosong
a = {}
print("==================================================================")
print("|      PROGRAM INPUT NILAI MAHASISWA MENGGUNAKAN DICTIONARY      |")
print("==================================================================")

# looping while , variabel inputan
while True :
    b=input("\n(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")  
    if (b.lower() == 't'):
        print('\nTambah Data Mahasiswa Baru')
        nama= input("Masukkan Nama\t\t: ")
        nim= input("masukkan NIM\t\t: ")
        nilaitugas= int(input("Masukkan Nilai Tugas\t: "))
        nilaiUTS= int(input("Masukkan Nilai UTS\t: "))
        nilaiUAS= int(input("Masukkan Nilai UAS\t: "))
        nilaiakhir= (0.30 * nilaitugas) + (0.35 *nilaiUTS) + (0.35 * nilaiUAS)
        a[nama]=nim,nilaitugas,nilaiUTS,nilaiUAS,nilaiakhir
        print("\nData Berhasil Ditambahkan!")
    elif (b.lower() == 'u') :
        print('\nMengedit Data Mahasiswa')
        nama = input("Masukkan Nama: ")
        if nama in a.keys() :
            nim= input("Masukkan NIM Baru\t: ")
            nilaitugas= int(input("Masukkan Nilai Tugas\t: "))
            nilaiUTS= int(input("Masukkan Nilai UTS\t: "))
            nilaiUAS= int(input("Masukkan Nilai UAS\t: "))
            nilaiakhir= (0.30 * nilaitugas) + (0.35 * nilaiUTS) + (0.35 * nilaiUAS)
            a[nama] = nim, nilaitugas, nilaiUTS, nilaiUAS, nilaiakhir
            print("\nData Berhasil Di Update!")
        else:                                                                                   
            print("Data tidak ditemukan!")
    elif (b.lower() == 'c'):
        print('\nCari Data Mahasiswa')
        nama = input("Masukkan Nama: ")
        if nama in a.keys() :
            print("\n                   DAFTAR NILAI MAHASISWA                   ")
            print("==============================================================")
            print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==============================================================")
            print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(nama, nim, nilaitugas, nilaiUTS, nilaiUAS, nilaiakhir)) 
            print("==============================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))
    elif (b.lower() == 'h'):
        nama = input("Masukkan Nama:  ")                                                        
        if nama in a.keys(): 
            del a[nama]
            print("Data Telah dihapus!")
        else:
            print("Data Mahasiswa Tidak Ada".format(nama)) 
    elif (b.lower == 'l') :
        if a.items():                                                                     
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("tampilkan data")
            i = 0
            for x in a.items() :
                i += 1
                print("|    {6} |   {0} |   {1} |   {2} |   {3} |   {4} |   {5}    |   ".format (x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
            print("==================================================================")
        else:
            print("\n                      DAFTAR NILAI MAHASISWA                    ")
            print("==================================================================")
            print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
            print("==================================================================")
            print("|                          TIDAK ADA DATA!                       |")
            print("==================================================================")
    elif (b.lower == 'k') :
        print('\n')
        print(21*'=')
        print("Nama\t: ZAHRA SYIFA ANNISA\nKelas\t: TI.21.C5\nNIM\t: 312110458")
        print(21*'=')
        break   
    else:
        print("Pilih menu yang tersedia: ")