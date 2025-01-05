dogru_sifre = input("Lütfen doğru şifreyi yazin : ")
print("Şifre ayarlandi. Şimdi şifrenizi doğrulayn.")

hak = 4
while hak > 0:

    sifre = input("Lütfen şifrenizi giriniz: ")
    
    if "kod" in sifre.lower():
        print("Şifre yanlis. Lütfen tekrar deneyin.")
        hak -= 1
        print(f"Kalan hakiniz: {hak}")
        continue
  
    if sifre == dogru_sifre:
        print("Şifre başariyla doğrulandi")
        break
    else:
        print("Yanliş şifre! Lütfen tekrar deneyin.")
        hak -= 1
        print(f"Kalan hakkiniz: {hak}")

if hak == 0:
    print("Deneme hakkiniz bitti..")
