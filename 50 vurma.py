for i in range(1, 11): 
    for x in range(1, 11):  
        sonuc = i * x
        if sonuc > 50:  
            continue 
        print(f"{i} x {x} = {sonuc}")
    print("-"*15)  
