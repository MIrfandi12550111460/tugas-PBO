from pathlib import Path

path =Path("guest_book.txt")
nama_list = []

while True:
    nama =input("nama pengguna adalah (ketik exit jika ingin keluar): ")
    
    if nama.lower() == "exit":
        for nama in nama_list:
            print("nama pengguna adalah: ",  nama)
        break
    nama_list.append(nama)
    path.write_text("\n" .join(nama_list))
