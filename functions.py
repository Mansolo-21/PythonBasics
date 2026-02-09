"""functions-perform specific tasks
def functionname():
    block of code

def demo():
    print("Good afternoon")
#calling the function
demo()

def greeting(name):
    print("Hello", name)
#calling
greeting("Johari")
greeting("Otieno")

#a fuction with multiple parameters
def studentInfo(first_name,age=18):
    print(f"Hello {first_name} you are {age} years old")
#callimg
studentInfo("Solomon",19)
studentInfo("Richard",18)
studentInfo("Anne")


def addNumbers(num1,num2):
    sum=num1+num2
    print("The sum is", sum)
addNumbers(5,7)

#function that calculates area of rectangle
def area(l,w):
    area=l*w
    print(f"The area of the rectangle with lenght {l} and width {w} equals to {area}")
area(70,50)
area(120,10)"""
#function that calculates area of a circle
def areaofcircle(r,a=3.14):
    areaofcircle=a*r
    print(f"The area of a circle with radius {r} is equal to {areaofcircle}")
areaofcircle(7)
