"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

##################   Solution #####################

# ask user for inputs

# ask user's name

user_name = input('What is your name?\n')

# ask user's age

user_age= input('What is your age?\n')

# calculate the year of birth from current year i.e. 2024
current_year=2024
user_birth_year=current_year-int(user_age) # typecasting- converting string input to integer

# calculate the year in which the user will turn 100 years old

final_output_year=user_birth_year+100

print("%s , you will turn 100 years old in %d" %(user_name,final_output_year))
