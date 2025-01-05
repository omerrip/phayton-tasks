sayilar = [
    [2, 5, 1, 7],
    [1, 6, 9, 3],
    [3, 1, 9, 10]
]

limit = 20
toplam = 0

for satir in sayilar:
    
    for sayi in satir:
  
        if sayi % 2 == 0:
            continue
   
        toplam += sayi
    
        if toplam > limit:
            print(f"Limit aşildi, Şu ana kadar bulunan tek sayilarin toplami: {toplam}")
            break
    if toplam > limit:
        break

if toplam <= limit:
    print(f"Tüm tek sayilarin toplami limitin altinda: {toplam}")
