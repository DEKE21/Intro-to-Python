import random
stop = 1
R = random.randint(1,10)
def rand(stop,R):
    while(stop == 1):
        I = int(input("Guess the number: "))
        if(R == I):
            print("You got it!!!!")
            stop = int(input("Would you like to play again? \n 1 for yes 0 for no: "))
            R = random.randint(1,10)

 
        elif(R>I):
            print("You guessed too low, try again")
        elif(R<I):
            print("You guessed too high, try again")
rand(stop,R)
    
    