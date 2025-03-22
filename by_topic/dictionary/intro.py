# dictionary in python
# a dictionary is a datatype in pyhon that store data in key-value pairs. Dictionary items (key -value pair ) are orderd
# changeable,and do not allow duplication

# key : must be unique and immutable (string, nubers, and tuples)
# value :can be any data type and does not need to be unique.

# how to create dictionary
#1  by curly braces{}
studnet = {1 : "class-X","name":"Madhav", "age":20}

#2 using dict() constructor
 # pass key- value pairs as keyword argumaent to dict()

person = (dict(name="madhav", age= 20, city = "mathura"))
print(person)

# using list of tuples
studnet_ = dict([("name","madhav"), ("age",20), ("grade", "A")])
print(studnet_)


# how to access dictonary values
# Access dictionary values by using the key name inside square brackets

print(studnet["name"])

