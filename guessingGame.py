import random
print("Guessing Number game")
number = random.randint(1,9)
chance = 0
print("Guess a number between 1-9")

while(chance<5):
    guess=int(input("Submit your answer"))
    if(guess==number):
        print("Congratulations")
        break
    
    elif(guess<number):
        print("Guess is low")

    else:
        print("Guess is high")

    chance+=1

if(not chance<5):
    print("You lose, the number was",number)






    