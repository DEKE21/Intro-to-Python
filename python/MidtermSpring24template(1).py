def main():
    again = 'y'
    while again == 'y' or again == 'Y':
        num1 = int(input("enter a number "))
        print(f"you entered {num1} as your first number")
        num2 = int(input("enter another number "))
        print(f"you entered {num2} as your second number")
        num1,num2 = validate(num1, num2)
  
        #your code here
        again = input('Do you want to do add two numbers again? (y/n): ')

def validate(n1,n2):
    #enter your code instead of pass - the other comment is a hint
    while n1< 0:
        n1 = int(input("enter a positive for the first number "))
    while n2 < 0:
        n2 = int(input("enter a positive for the second number "))
    n1,n2 = add(n1,n2)

    return(n1,n2)
         
    #return num

def add(num1, num2):
    #enter your code instead of pass
     s = num1+num2
     s = outputprint(s)
     return (num1,num2)
def outputprint(ans):
    #enter your code instead of pass
     print(f"the sum of the numbers is {ans}")

   
    
main()
