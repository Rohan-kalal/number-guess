import random

randomnumber=random.randint(1,100)
userguess=None
guesses = 0

while(userguess != randomnumber):
  userguess=int(input("Number please : "))
  guesses += 1
  if(userguess==randomnumber):
    print("your guess is right")
  else:
    if(userguess>randomnumber):
        print("your guess is wrong! enter smaller number")
    else:
        print("your guess is wrong! enter larger number")

