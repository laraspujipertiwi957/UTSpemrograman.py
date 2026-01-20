def luaspersegi(sisi) :
    return sisi * sisi

def kelilingpersegi(sisi) :
    return 4 * sisi

def luaspersegipanjang(panjang,lebar) :
    return panjang * lebar

def kelilingpersegipanjang(panjang,lebar) :
    return 2 * (panjang + lebar)

def luassegitiga (alas,tinggi,sisi_a,sisi_b,sisi_c) :
    return 0.5 * alas * tinggi

def kelilingsegitiga (alas,tinggi,sisi_a,sisi_b,sisi_c) :
    return alas + sisi_a + sisi_b + sisi_c

def luaslingkaran (jari_jari) :
    return 1.4 * jari_jari **2

def kelilinglingkaran (jari_jari) :
    return 2* 3.14159 * jari_jari


nama = input("Masukkan Nama Anda:")

print(nama,", selamat datang di pemrograman dasar")

print("pilih bangun datar:")
#print("1 persegi")
#print("2 persegi panjang")
#print("3 segitiga")
#print("4 lingkaran")

daftar_bangun_datar = ("1.persegi", "2. persegi panjang", "3. segitiga", "4. lingkaran")

# for bangun_datar in daftar_bangun_datar:
#     print(bangun_datar)

i = 0

while i < len(daftar_bangun_datar):
    print(daftar_bangun_datar[i])
    i += 1

pilihan = int(input("masukkan pilihan anada (1-4:"))

while True:
    if pilihan == 1:
        sisi = int(input("masukkan sisi persegi: "))
        print("luas persegi adalah:", luaspersegi(sisi))
        print("keliling persegi adalah:", kelilingpersegi(sisi))
    elif pilihan == 2:
        panjang,lebar = int(input("masukkan panjang,lebar persegi panjang:"))
        print("luas persegi panjang adalah:", luaspersegipanjang(panjang,lebar))
        print("keliling persegi panjang adalah:", kelilingpersegipanjang(panjang,lebar))
        
    elif pilihan == 3:
        alas,tinggi,sisi_a,sisi_b,sisi_c = int(input("masukkan alas,tinggi,sisi_a,sisi_b,sisi_c segitiga:"))
        print("luas segitiga adalah:", luassegitiga(alas,tinggi,sisi_a,sisi_b,sisi_c))
        print("keliling segitiga adalah:", kelilingsegitiga(alas,tinggi,sisi_a,sisi_b,sisi_c))
    elif pilihan == 4:
        jari_jari = int(input("masukkan jari_jari lingkaran: "))
        print("luas lingkaran adalah:", luaslingkaran(jari_jari))
        print("keliling lingkaran adalah:", kelilinglingkaran(jari_jari))
        
    else:
        print("pilihan tidak tersedia,coba lagi!")
        
    lagi = input ("apakah anda ingin menghitung lagi? (y/n):")

    if(lagi == "y"):
        print("silahkan jalankan program ulang")
        continue
    else:
        print("terima kasih", nama)
        break
