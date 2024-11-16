import random

welcome_message = "WELCOME TO CUYPY GAME"
cuypy_posision = random.randint(1, 4)
tidak = "N"
iya = "Y"

print("***************************")
print(f"** {welcome_message} **")
print("***************************")

nama_user = input("Masukan Nama Kamu: ")

bentuk_goa = "'|_|'"
goa_kosong = [bentuk_goa] * 4

goa = goa_kosong.copy()

print('|'.join(goa_kosong))

goa[cuypy_posision - 1 ] = "|0_0|"


print(f'''Halo {nama_user}! Coba perhatikan goa di bawah ini
{goa_kosong}
''')

pilihan_user = int(input("Menurut kamu cupay ada di mana? [1 / 2 / 3 / 4]: "))

konfirmasi = input(f"Apakah kamu yakin dengan pilihan mu {iya} / {tidak}:")
    
if konfirmasi.upper() == iya:
    if pilihan_user == cuypy_posision:
        print (f"{goa}, \n selamat kamu menag!")
    else:
        print (f"{goa}, \n Maaf Kamu Kalah!")
else:
    print ("Silakan Yakin Dengan Pilihan Mu")