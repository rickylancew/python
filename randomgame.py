# Name: Ricky Williams
# Date: 10-22-2022

'''
Random number generator game to gain familiarity using sys package and sys.argv.
'''

import random, sys

number_of_attempts = 0
guessed_correctly = False
try:
	first_num = int(sys.argv[1])
	second_num = int(sys.argv[2])
except:
	print("Please enter valid integer parameters and try again. ")
else:
	random_num = random.randint(first_num, second_num)
	while guessed_correctly != True:
		number_of_attempts += 1
		user_guess = int(input(f"Please enter a valid guess from {first_num} to {second_num}: "))
		#print(random_num)
		if user_guess == random_num:
			guessed_correctly = True
			print("That's correct!")
			print(f"Number of attempts until correct guess : {number_of_attempts}")
			break

