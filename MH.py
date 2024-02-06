H = input("Enter a hour 0 - 23\n")
M = input("Enter the minutes 0 - 59\n")
FF(H,M)

def FF(): 
     if(H >23 or H < 0 or M >59 or M < 0):
        print("Error: Value out of range")
     elif(H <=23 or H >= 0 or M <=59 or M >= 0):
        print(f"You entered {H} Hours and {M} Minutes")
 
 



 