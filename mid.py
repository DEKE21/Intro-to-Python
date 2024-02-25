def main():
        stop = 1
        while (stop != 0):
            print("I am going to ask for two positive numbers and add them together.")
            print("I will print out the numbers and the total for you.")
            num1 = int(input("enter a number "))
            print(f"you entered {num1} as your first number")
            num2 = int(input("enter another number "))
            print(f"you entered {num2} as your second number")
            sum = 0
            num1,num2,sum = calcsum(num1, num2,sum)
         
            print(f"the sum of the numbers is {sum}")
            ex = int(input("would you like to continue? 1 for yes 0 for no"))
            stop = ex
                    
            
            
        
    

    


def calcsum(num1, num2,sum):
    while num1 < 0:
        num1 = int(input("enter a positive for the first number "))
    while num2 < 0:
        num2 = int(input("enter a positive for the second number "))
    sum= num1 + num2
    return(num1,num2,sum)



 
main()
