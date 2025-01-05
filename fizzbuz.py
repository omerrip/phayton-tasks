for sayi in range(1, 101):
    if sayi % 3 == 0 and sayi % 5 == 0:
        pass  
    elif sayi % 3 == 0:
        print(f"{sayi}: Fizz") 
    elif sayi % 5 == 0:
        print(f"{sayi}: Buzz") 
    else:
        print(sayi)  
