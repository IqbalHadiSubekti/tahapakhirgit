def menuliskan_perkenalan(nama,kelas,sekolah):
	file=open("daftar_nama.txt","a+")
	data = file.write("Nama: %s \n"%(nama))
	data = file.write("Asal: %s \n"%(kelas))
	data = file.write("Sekolah: %s \n"%(sekolah))
	
def tampilkan_perkenalan():
	file = open("daftar_nama.txt","r")
	print("===tampilkan perkenalan===")
	print(file.read())

def option():
	print("Pilih salah satu dari tiga pilihan berikut :")
	print("1. Menuliskan perkenalan")
	print("2. Tampilkan perkenalan")
	print("3. Keluar program")
	pilihan = int(input("Masukan pilihan anda :"))
	return pilihan
	
pilihan = True
while(pilihan<3):
	pilihan = option()
	if (pilihan ==3):
		break;
	if (pilihan == 1):
		nama = str(input("Masukan nama :"))
		kelas = str(input("Masukan kelas :"))
		sekolah = str(input("Masukan sekolah :"))
		menuliskan_perkenalan(nama,kelas,sekolah)
	elif(pilihan ==2):
		tampilkan_perkenalan
	