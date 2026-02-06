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
print(student["student name"])
print(student["age"])
print(student["course"])