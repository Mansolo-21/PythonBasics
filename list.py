""" list - used to store multiple items in a single variable
-is ordered is changeable duplicates
"""
students=["Johari","Mary","Keter","Jane"]
my_numbers=[78,76,56,23,23,12,43,45,76]
print(students)
print(my_numbers)
print(type(students))
print(type(my_numbers))

#len-length
print(len(students))
print(len(my_numbers))

#accessing list items
print(students[0])
print(students[3])

#modify list item
print(students)
students[1]="Angela"
print(students)

#List methods =(append(),remove(),pop())
#append - adds an item at the end
students.append("John")
print(students)

#remove
students.remove("Jane")
print(students)

#insert-insert an item at a specific index
students.insert(1,"Lewis")
print(students)

#pop
students.pop()
print(students)

#looping through a list
for x in students:
    print(x)