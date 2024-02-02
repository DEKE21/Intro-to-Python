# main.py
M = 10 
C = 10 
STOP = 1

while(STOP !=101):    
    if(M<=0):
        print("M is out of stock")
    elif(C<=0):
        print("C is out of stock")
    B = input("Would you like to buy anything?"
    "0 to exit and print stock?")

    if(B=="Y"or B=="y" or B== "Yes" or B== "yes"):
        A = str(input("\"muffin\" for a muffin, \"cupcake\" for a cupcake"))
        if(A=="muffin"or A== "Muffin"):
            M= M - 1
        elif(A=="Cupcake" or A=="cupcake"):
            C = C-1
    elif(B=="0"):
        STOP = 101
        print(f"you have {M} M and {C} C")

 