try:
    angka1 = input("Masukkan angka pertama: ")
    angka2 = input("Masukkan angka kedua: ")

    hasil = int(angka1) + int(angka2)

    print("Hasil penjumlahan:", hasil)

except ValueError:
    print("Hasil Input harus berupa angka ya ^u^")