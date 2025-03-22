# you can create list in python by placing comma-separated values between sqare brackets [].
# list can contain elements of different data type, incletding other lists.

# sytax: list name = [element1, element2, element3, ...]
# ex.
# mixed data types
# mixed = [1,"hello", 3.14, True]


# 1-------
# nasted list and list indexing
nested = [1,[2,3],[True,"hello"]]

# accessing list elements - indexing
# you can access elements in a list by referring to their index.
# python uses zero- based indexing, meaning the first element has an index of 0
# you can use negitive index system for geting value from end side of the list

print(nested[2])        # for getting one element from list
print(nested[2][1])
print(nested[-1])     # for getting element from list inside list
print(nested)



#2-------

# list slicing
#slicing allows you to access a range of elements in a list. you specify the start and stop 
#indices, and pyhon return a new list containing the specified elements.
#syntax : list_name[start:stop:step]

number = [2,45,34,7876,54,88]

#slice from index 1 to 3 
print(number[1:4])
#slice all alternate elements 
print(number[::2])
#reverce list
print(number[::-1])



#3------

# modifying list
# lists are mutable, meaning you can change their content after creation. you can add, 
#remove, or change elements in a list.

# inital list:
frute = ["apple", "banana", "charry"]


#changing element
frute[1] = "mango"
print(frute)

#adding an element
frute.append("blueberry")
print(frute)

# removeing an element
frute.remove("charry")
print(frute)

