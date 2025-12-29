import random #importing module
playing = True #initialise
number = str(random.randint(10,20)) #random in-built function
print("i will genarate a number from 0 to 9, and you have to guess the number one digit at a time")
print("the game ends where you get 1 hero!")
#iterate loop till the condition is true
while playing:
    guess = input("give me your best guess! \n ")
    if number == guess:
      print("you win the game")
      print("the number was",number)
      break
    else:
      print("your guess isn't quite right, try again. \n")   