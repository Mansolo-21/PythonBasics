"""#elif - used to test multiple conditions

#if...elif...else
if condition1: 
    # execute this block of code if condition1 is true
elif condition2: 
    # execute this block of code if condition2 is true
elif condition3: 
    # execute this block of code if condition3 is true
else: 
    # execute this block of code if all conditions are false
    
#a program asks user for marks then compute the grade
#80-100 =A
#70-80 =B
#60-70 =C
#50-60 =D
#Else = Fail

grade=int(input("Enter your marks: "))
if grade >= 80 and grade <=100:
    print("Your grade is A")
elif grade >=70 and grade <80:
    print("Your grade is B")
elif grade >=60 and grade <70:
    print("Your grade is C")
elif grade >=50 and grade <60:
    print("Your grade is D")
else:
    print("You have failed")"""
    
#a program that asks user age and prints
#18-30 young adult
#30-45 adult
#45-65 mature adult
#65-100 elderly
#<18-baby

user_age=int(input("Enter your age: "))

if user_age >=18 and user_age < 30 :
    print("Your a young adult")
elif user_age >=30 and user_age < 45:
    print("Your an adult")
elif user_age >=45 and user_age <65:
     print("Your a mature adult")
elif user_age >65 :
    print("Your an elder")
else:
   print("Your a baby")
    
    