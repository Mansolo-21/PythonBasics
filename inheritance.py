#inheritance - a child class inherits attributes and methods
#super/parent class
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        return f"hello"
    def supermethod(self):
        return f"Hello form a method in a super class"
#add a class cat that inherits from animal
class Cat(Animal):
    def speak(self):
        return f"meow meow"

#child/sub class   
class Dog(Animal):
    def speak(self):
        return f"Bark Bark"
    def chrome(self):
        return f"Hello from a method in dog class"

#create a dog object
mydog=Dog("Bob",9)
print(mydog.name)

#call parent method
print(mydog.supermethod())

#overiding method
print(mydog.speak())

#calling our own method
print(mydog.chrome())

#create a cat object
mycat=Cat("Whiskers",13)

#call the speak method
print(mycat.speak())

#call me the supermethod
print(mycat.supermethod())