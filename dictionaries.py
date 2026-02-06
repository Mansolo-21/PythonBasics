#dictionaries- used to store data values in key:value pairs.
# written with curly brackets, and have keys and values:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary items are ordered, changeable, and do not allow duplicates.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#len()
print(len(thisdict))

#type()

print(type(thisdict)) 

#remove
thisdict.popitem() 
print(thisdict)



student={
        "Student name":"John",
        "age":18,
        "course":"Cybersecurity"
    }

print(student)
print(type(student))

#accessing dictionary items
print(student["Student name"])
print(student["age"])
print(student["course"])

#adding key:value pair
student["grade"]="A"
print(student)

#updating a value
student["course"]="Web Development"
print(student)

#accessing all keys called keys
print(student.keys())

#accessing all values, values()
print(student.values())

#accessing all keys and values
print(student.items())

#loop thru all keys
for x in student.keys():
    print(x)
    

#loop thru all values
for y in student.values():
    print(y)
    

#loop thru all items
for z in student.items():
    print(z)