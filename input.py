"""first_name=input("Enter your name: ")
fav_book=input("What is your favorite book? ")
print("Hello, " + first_name + "!")
print("Your favorite book is: " + fav_book)
x=input("Enter first number: ")
y=input("Enter second number: ")
#output of input is always a string, so we need to convert it to an integer before performing addition

sum=int(x)+int(y)
print("The sum is: " + str(sum))"""

    #A program that asks user for 5 numbers and prints their average
first_mark=input("Enter first mark: ")
second_mark=input("Enter second mark: ")
third_mark=input("Enter third mark: ")
fourth_mark=input("Enter fourth mark: ")
fifth_mark=input("Enter fifth mark: ")
average=(int(first_mark)+int(second_mark)+int(third_mark)+int(fourth_mark)+int(fifth_mark))/5
print("Average =", (average))