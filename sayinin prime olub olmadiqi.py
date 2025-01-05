baslangic = int(input("Başlangiç sayisini giriniz: "))
bitis = int(input("Bitiş sayisini giriniz: "))


prime_sayilar = []
for sayi in range(baslangic, bitis + 1):
    if sayi < 2:
        continue
    if sayi % 2 == 0 and sayi != 2:
        continue

    bolen = 0
    for i in range(2,int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            bolen = 1
            break
    
    if bolen == 0:
        prime_sayilar.append(sayi)

print(f"{baslangic} ile {bitis}arasindaki asal sayilar: {prime_sayilar}")
