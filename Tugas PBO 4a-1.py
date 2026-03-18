from pathlib import Path

path =Path("guest.txt")
nama =input("masukkan nama anda: ")
path.write_text(nama)
content =path.read_text()

print("nama anda adalah: ", content)
