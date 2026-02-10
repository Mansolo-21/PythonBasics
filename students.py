#class- is a blueprint for creating object
#object is an vinscance of a class
class Student:
    #constructor
    #runs automatically when an object is created
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
        
    def __str__(self):
        return f"The student's name is {self.name} ,is {self.age} and does {self.course}"
#create an object
#object is an instance of a class
#objectname=classsname(values)
student1=Student("Johari",18,"IT")
student2=Student("Michael",18,"booning")
print(student1)
print(student2)