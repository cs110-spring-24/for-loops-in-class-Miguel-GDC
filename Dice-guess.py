import random
dice = random.randint(1, 6)

user = input ("Enter your guess: ")
user = int(user)

if user == dice:
	print("You got it!")
else:
	print("Nope, it was" dice)