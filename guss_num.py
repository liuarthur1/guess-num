import random

r = random.randint(1,100)


while True:
	num	= int(input("Type the number :"))

	if num == r:
		print("You guess right!!")
		break
	elif num > r:
		print("You Guess bigger then answer!")
	else:
		print("You Guess small than answer!")

