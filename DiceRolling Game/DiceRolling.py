import random


x = " "
y = input("Hit space for rolling!")
if y == " " :
    while x == " ":
        
        count= random.randint(1,6)
        
        if count == 1:
            print("-----------")
            print("|         |")
            print("|    0    |")
            print("|         |")
            print("-----------")
        
        if count == 2:
            print("-----------")
            print("|         |")
            print("|  0   0  |")
            print("|         |")
            print("-----------")
        
        if count == 3:
            print("-----------")
            print("|    0    |")
            print("|    0    |")
            print("|    0    |")
            print("-----------")
            
        if count == 4:
            print("-----------")
            print("|  0   0  |")
            print("|         |")
            print("|  0   0  |")
            print("-----------")
            
        if count == 5:
            print("-----------")
            print("|  0   0  |")
            print("|    0    |")
            print("|  0   0  |")
            print("-----------")
            
        if count == 6:
            print("-----------")
            print("|  0   0  |")
            print("|  0   0  |")
            print("|  0   0  |")
            print("-----------")
        
        
        x = input("Hit space for rolling!")
    

