print('''
NAMA : Muh. Arifatwa
Nim  : D0221081
Kelas : Informatika F  ''')
print("==================================\n")

print("Menghitung luas persegi".center(70))
p = float(input("Masukan panjang : "))
l = float(input("Masukan lebar :"))
persegi = p*l
print("Luas persegi adalah :" + str(persegi))

print("==================================\n")
print("Menghitung luas lingkaran".center(70))
r = int(input('masukan jari-jari lingkaran : '))
phi = 3.14
L = phi * (r*r)
print('Luas lingkaran dengan jari-jari {} adalah {}'.format(r,L))

print("==================================\n")
print("Menghitung luas Segitiga".center(70))
a = float(input("Masukan panjang alas : "))
t = float(input("Masukan tinggi segitiga : "))
luas = 0.5*a*t
print("Luas segitiga adalah :"+str(luas))