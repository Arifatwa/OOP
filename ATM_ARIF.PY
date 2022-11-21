'''
ATM : MUH. ARIFATWA

'''
def atm():
    print("SELAMAT DATANG ATM MUH.ARIFATWA")
    print("PILIH OPTION  : ")
    print("1.CEK SALDO")
    print("2.TARIK UANG")
    print("3.TABUNG UANG")
    pilihan = int(input("Silahkan Masukkan Pilihan : "))
    if pilihan == 1 :
        print("Uang kamu berjumlah Rp.5.000.000")
    elif pilihan == 2 :
        print("uang kamu berjumlah Rp.5.000.000, mau ambil berapa")
        print("1. 100.000")
        print("2. 200.000")
        uang_kamu = 5000000
        pilihan2 = int(input("Pilih option : "))
        if pilihan2 == 1:
            hasil = uang_kamu - 100000
            print("Uang kamu sekarang berjumlah Rp. :",hasil)
        elif pilihan2 == 2:
            hasil = uang_kamu - 200000
            print("Uang kamu sekarang berjumlah Rp. :",hasil)
        else:
            print("keyboard anda salah!")
    elif pilihan == 3:
        uang_kamu = 5000000
        print("Uang berjumlah Rp.200.000,mau ambil berapa.?")
        pilihan = int(input("masukkan jumlah uang : "))
        hasil = uang_kamu + pilihan
        print("Jumlah uang kamu sekarang adalah Rp. : ",hasil)
    else:
        print("Anda salah, silahkan masukkan ulang : ")
atm()