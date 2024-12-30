import random #importing module
playing = True #initialise
number = str(random.randint(10,20)) #random in-built function

print("I will generate a number from 0 to 9, and you have to guess the number one digit at a time.")
print("the game ends when you get 1 hero!")
#iterate loop till the condition is true while playing:
while playing:
  guess = input("Give me your best! \n")
  if number == guess:
    print("You win the game")
    print("the number was",number)
    break
else:

  print("your guess isn't quite right, try again. \n")