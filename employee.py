#class- is a blueprint for creating object
#object is an instance of a class
#object-artibutes and methods
class Employee:
    def __init__(self,first_name,second_name,department,salary):
        self.first_name=first_name
        self.second_name=second_name
        self.department=department
        self.salary=salary
        
    def __str__(self):
        return f"{self.first_name} {self.second_name} is in the department of {self.department} and earns {self.salary} per month"
    
    def __annualsalary__(self):
        return f"{self.salary*12}"
    
    def __full_name__(self):
        return f"{self.first_name} {self.second_name}"
employee1=Employee("John","Mwangi","Finance",150000)
employee2=Employee("Maria","Abok","Business",350000)    
employee3=Employee("Richard","Kinyanjui","Marketing",250000)
print(employee1)
print(employee2)
#returns annual salary
print(f"{employee1.first_name} {employee1.second_name} earns Ksh {employee1.__annualsalary__()} a year")
print(f"{employee2.first_name} {employee2.second_name} earns Ksh {employee2.__annualsalary__()} a year")
print(f"{employee3.first_name} {employee3.second_name} earns Ksh {employee3.__annualsalary__()} a year")
#returns full name
print(employee1.__full_name__())
print(employee2.__full_name__())
print(employee3.__full_name__())