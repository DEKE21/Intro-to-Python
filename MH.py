def main(): 
   FF()
def FF():
   e= 0
   while(e!=1):
      H = int(input("Enter a hour 0 - 23\n"))
      M = 0
      if(H>23 or H < 0):
         print("Error: Value out of range")
      elif(H<24 and H > 0):
         M = int(input("Enter the minutes 0 - 59\n"))
      if(M > 59  or M < 0):
         print("Error: Value out of range")
      elif(M < 60 and M >= 0):
         if(H < 24 and H >= 0 and M <60 and M >= 0):
            print(f"You entered {H} Hours and {M} Minutes")
main()        

 