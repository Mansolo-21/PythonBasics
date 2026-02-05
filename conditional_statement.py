#if statement
"""
if-statement specifies a block of code to be executed if a specified condition is true.
if condition:
    # block of code to be executed

"""
x=20
if x <10:
    print(f"{x} is less than 10")
"""if...else statement
if condition:
    # block of code to be executed
else:
    block of code to be executed if the condition is false

age=67
if age >=18:
    print("You are eligible to vote")
else:   
    print("You are not eligible to vote")
    
#a program that asks user for their age and checks ifthey can drive
user_age=int(input("Enter your age: "))
if user_age >=18:
    print("You can drive")
else:
    print("YOU CANT DRIVE LITTLE BRO")"""
    
    
#a program that asks for a number and checks if it is even or odd
number=int(input("Enter a number: "))
if number % 2 ==0:    
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

#a program that asks user for two numbers and prints the greater number
first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
else:
    print(f"{second_number} is greater than {first_number}")
    

