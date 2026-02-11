class Car:
    def __init__(self,brand,color,year_of_manufacturer):
        self.brand=brand
        self.color=color
        self.year_of_manufacturer=year_of_manufacturer
        
    def __str__(self):
        return f"We have a {self.color} {self.brand} manufactured from the year {self.year_of_manufacturer} "
        
car1=Car("Audi","Black","1994")
car2=Car("Volkswagen","Red","1954")
car3=Car("BMW,","Green","1989")
print(car1)
print(car2)
print(car3)