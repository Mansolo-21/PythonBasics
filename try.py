""" 
try:
    block of code
except
    code that runs if error happens
    
"""
# try:
#     num=int(input("Enter a number, "))
#     print(10/num)
# except:
#     print("You cannot divide a number by 0")
    
# #example
# try:
#     print()    
# except NameError:
#     print("The variable is not defined")
try:    
    with open('wawr.txt','r')as x:
        print(x)
except FileNotFoundError:
    print("The file does not exist")