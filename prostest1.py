user = {
    'username' : 'M. Fadhiilah Hisyam',
    'nim' : '2309116066',
    'password' : 'fadhiil123'
}

def konversi(kg, satuan):
    if satuan == "lb":
        return kg * 2.20462
    elif satuan == "ons":
        return kg * 35.274
    elif satuan == "g":
        return kg * 1000
    else:
        return None
    
def login():
    while True:
        username = input("Masukkan nama : ")
        nim = input("Masukkan NIM : ")
        password = input("Masukkan password : ")

        if username == user['username'] and password == user['password'] and nim == user['nim']:
            break
        else:
            print("Data yang anda masukkan salah")

print("======================================")
print("                LOGIN                 ")
login()
print("======================================")
print("               KONVERSI               ")
kg = float(input("Masukkan massa dalam kilogram(kg) : "))
while True:
    satuan = input("Pilih satuan konversi (lb/ons/g) : ").lower()

    hasil = konversi(kg, satuan)

    if hasil is not None:
        print(f"{kg} kg sama dengan {hasil:.2f} {satuan}")
        break
    else:
        print("Satuan konversi tidak valid. Harap pilih lb, ons, atau g")
print("======================================")