def main():
   hour = int(input("Enter a hour 0 - 23\n"))
   min = int(input("Enter the minutes 0 - 59\n"))
   hour,min = FF(hour,min)
   print(f"You entered {hour} Hours and {min} Minutes")

def FF(M,H):  
   while(H>23 or H < 0):
      print("Error: Value out of range")
   while(M > 59  or M < 0):
      print("Error: Value out of range")
   return (M,H)
main()        

 