#functions which return a value
#function that add two numbers and returns the sum
def addTwonumbers(a,b):
    sum=a+b
    return sum

#calling the function
result=addTwonumbers(5,7)
print("The sum is", result)

#Method 2
print(addTwonumbers(5,7))

#funtion that multiplies  3 numbers
def multiplyThreeNumbers(x,y,z):
    product=x*y*z
    return product
result=multiplyThreeNumbers(2,3,4)
print("The product is", result)


#FUNCTION THAT CHECKS IF A NUMBER IS EVEN OR ODD
def evenorodd(number):
    if  number%2==0:
        print(f"{number} is even number")
    else:
        print(f"{number} is an odd number")
        
#get user input
num=int(input("Enter a number, "))
evenorodd(num)

#maximum of 2 numbers
def maximum(a,b):
    if a > b:
        print(f"{a} is larger than {b}")
    else:
        print(f"{b} is larger than {a}")

maximum(3,6)

#or
def maximum(x,y):
    return max(x,y)
print(maximum(67,76))


