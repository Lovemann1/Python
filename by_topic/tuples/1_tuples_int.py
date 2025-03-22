#tuples in python
# a tuble is a collection of items in Python that is ordered , unchangeable (immutable) and allow duplicate value.
# tubles are used to store multiple item in a single varibale.

# note ordered- tuple item have a defined order, but that order will not change
# example:
fruits = ("apple", "orange", "cherry","apple")
print(fruits)


#1  create tuple 
#  create tuple in pyton() by parantheses
num = (23,54,33,5)
print(num)

# create tuple without parantheses (comma-separated)
num_ = 34,36,45,33,7
print(num_)

# create tuple by using tuple() constructor 
list_ = ["apple", 2, (3,4)]
tuple_ = tuple(list_)               # usful if you converting values form list or any other datatpye
print(tuple_)



a = "True"
b = bool(a)
print(type(b))


