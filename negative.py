sayilar = [10, -5, 0, 20, -15, 30, 0, -25, 40]

for sayi in sayilar:
    if sayi < 0:  
        continue
    elif sayi == 0:
        pass
    else: 
        print(f"Pozitif sayi: {sayi}")
