# main.py
M = 10 
C = 10 
STOP = int(input("CODE NUMBER?"))

while(STOP !=101):    
    if(M<=0):
        print("you are out of M")
    elif(C<=0):
        print("You are out of C")
    B = input("Would you like to buy?")

    if(B=="Y"or B=="y" or B== "Yes" or B== "yes"):
        A = str(input("Do you want a M or C "))
        if(A=="m"or A== "M"):
            M= M - 1
        elif(A=="C" or A=="c"):
            C= C - 1 
        else:
            print("no")
    elif(B=="0"):
        STOP = 101
        print(f"you have {M} M and {C} C")

 