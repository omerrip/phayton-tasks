kelimeler = []
print("Lütfen 4 kelime giriniz:")

for _ in range(4):
    kelime = input("Kelime: ")
    kelimeler.append(kelime)

i = 0  
while i < len(kelimeler):
    kelime = kelimeler[i]

    if len(kelime) < 3:
        pass  
    else:

        if kelime != kelime[::-1]: 
            print(f"'{kelime}' bir palindrom değil. ")
            break
        else:
            print(f"'{kelime}' bir palindromdur.")
    
else:
    print("Tüm kelimeler palindromdur.")
