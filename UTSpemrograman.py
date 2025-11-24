angka = input("Masukkan sebuah bilangan: ")


if not angka.isdigit():
    print("Input tidak valid! Harap masukkan angka saja.")
else:
  
    print(f"\nAnda memasukkan bilangan {angka} dimana:")

   
    tempat_nilai = ["satuan", "puluhan", "ratusan", "ribuan",
                    "puluh ribuan", "ratus ribuan", "jutaan"]

   
    angka_terbalik = angka[::-1]

    
    hasil = []

    for i in range(len(angka_terbalik)):
        digit = angka_terbalik[i]
        posisi = tempat_nilai[i]
        hasil.append((digit, posisi))

 
    for digit, posisi in reversed(hasil):
        print(f"{digit} merupakan {posisi}")