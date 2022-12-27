'''
nama : Muh.Arifatwa
Nim : D0221081
Kelas : informatika F

'''

# class bangun ruang    
class volume_bangun_ruang:
    def volume(self):
        pass
    
class Kubus(volume_bangun_ruang):
    def __init__(self, sisi):
        self.sisi = sisi
        
    def volume(self):
        return self.sisi * self.sisi * self.sisi
    
class Limas(volume_bangun_ruang):
    def __init__(self, alas, tinggi_alas, tinggi_limas):
        self.alas = alas
        self.tinggi_alas = tinggi_alas
        self.tinggi_limas = tinggi_limas
        
    def volume(self):
        return 1/3 * ((1/2 * self.alas * self.tinggi_alas) * self.tinggi_limas)

class Tabung(volume_bangun_ruang):
    def __init__(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
        
    def volume(self):
        return 22/7 * self.jari_jari * self.jari_jari * self.tinggi

# class bangun datar
class luas_bangun_datar:
    def luas(self):
        pass

class Persegi(luas_bangun_datar):
    def __init__(self, sisi):
        self.sisi = sisi
    def luas(self):
        return self.sisi * self.sisi

class Segitiga(luas_bangun_datar):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas(self):
        return self.alas * self.tinggi / 2
    
class Lingkaran(luas_bangun_datar):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari
        
    def luas(self):
        return 22/7 * self.jari_jari * self.jari_jari


# menu utama

def menu_pilihan():
    while True:
        print(" ")
        print("=" * 50)
        print(" menghitung luas volume ".center(50,"="))
        print("=" * 50)
        print("\n1. Luas \n2. Volume \n3. Keluar")
        pilihan = int(input("\nMasukkan Pilihan : "))
        if pilihan == 1:
            menu_luas()
            
        elif pilihan == 2:
            menu_volume()
        
        elif pilihan == 3:
            print(" ")
            print("-" * 50)
            print(" keluar dari program ".center(50,"="))
            print("-" * 50)
            exit()
        
        else:
            print(" ")
            print("Perintah Tidak Ditemukan !")
            print("Silahkan Pilih Menu Yang Tersedia")
            
# menu luas bangun datar 
def menu_luas():
    while True:
        print(" ")
        print("=" * 50)
        print(" program menghitung luas ".center(50, "="))
        print("=" * 50)
        print("\n1. Persegi \n2. Segitiga \n3. Lingkaran \n4. Kembali")
        subpilihan = int(input("\nMasukkan Pilihan : "))
        if subpilihan == 1:
            print(" ")
            print("-" * 50)
            print(" menghitung luas persegi ".center(50,"="))
            print("-" * 50)
            sisi = float(input("Masukkan Sisi Persegi : "))
            persegi = Persegi(sisi)
            print("Luas Persegi : ", persegi.luas())
            print("-" * 50)
            print(" ")

        elif subpilihan == 2:
            print(" ")
            print("-" * 50)
            print(" menghitung luas segitiga ".center(50,"="))
            print("-" * 50)
            alas = float(input("Masukkan Alas Segitiga : "))
            tinggi = float(input("Masukkan Tinggi Segitiga : "))
            segitiga = Segitiga(alas, tinggi)
            print("Luas Segitiga : ", segitiga.luas())
            print("-" * 50)
            print(" ")

        elif subpilihan == 3:
            print(" ")
            print("-" * 50)
            print(" menhitung luas lingkaran ".center(50,"="))
            print("-" * 50)
            jari_jari = float(input("Masukkan Jari-Jari Lingkaran : "))
            lingkaran = Lingkaran(jari_jari)
            print("Luas Lingkaran : ", lingkaran.luas())
            print("-" * 50)
            print(" ")

        elif subpilihan == 4:
            menu_pilihan()
        else:
            print(" ")
            print("Perintah Tidak Ditemukan")
            print("Masukkan Perintah Dengan Benar!")

# menu volume bangun ruang : kubus, limas, dan tabung.
def menu_volume():
    while True:
        print(" ")
        print("=" * 50)
        print(" menghitung volume ".center(50, "="))
        print("=" * 50)
        print("\n1. Kubus \n2. Limas Segitiga \n3. Tabung \n4. Kembali")
        subpilihan = int(input("\nMasukkan Pilihan : "))
        if subpilihan == 1:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG VOLUME KUBUS ".center(50,"="))
            print("-" * 50)
            sisi = float(input("Masukkan panjang sisi : "))
            kubus = Kubus(sisi)
            print("Volume Kubus : ", kubus.volume())
            print("-" * 50)
            print(" ")
            
        elif subpilihan == 2:
            print(" ")
            print("-" * 50)
            print(" menghitung limas segitiga ".center(50,"="))
            print("-" * 50)
            alas = float(input("Masukkan nilai alas : "))
            tinggi_alas = float(input("Masukkan  nilai tinggi : "))
            tinggi_limas = float(input("Masukkan tinggi limas : "))
            limas = Limas(alas, tinggi_alas, tinggi_limas)
            print("Volume Limas : ", limas.volume())
            print("-" * 50)
            print(" ")

        elif subpilihan == 3:
            print(" ")
            print("-" * 50)
            print(" PROGRAM MENGHITUNG VOLUME TABUNG ".center(50,"="))
            print("-" * 50)
            jari_jari = float(input("Masukkan Jari-Jari Lingkaran Tabung : "))
            tinggi = float(input("Masukkan Tinggi Tabung : "))
            tabung = Tabung(jari_jari, tinggi)
            print("Volume Tabung : ", tabung.volume())
            #print("Volume Tabung : ", round(tabung.volume())) ---> jika ingin menggunakan pembulatan
            print("-" * 50)
            print(" ")
            
        elif subpilihan == 4:
                menu_pilihan()
        else:
            print(" ")
            print("Perintah Tidak Ditemukan")
            print("Masukkan Perintah Dengan Benar!") 
            
menu_pilihan()