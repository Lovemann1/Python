#1 slicing 
# slicing allows you to access a range of elements in a tuble. you can specify
# and stop indices, and python returns a new tuple containing the specefied elements.
# syntex tuple_name[start:stop:step]


num = (10,34,53,67,70,34,54,66,7,36)
print(num[2::2])

a = (("a"))
print(type(a))      #if you have a single element in bracket it we not a tuple so
                    # you have to add a addion , after that to 
                    # make it a tuple
                
a = ("a",)



#2 -- tuple operations

#1. concatenation
# you can join two or more tuples using the + operater.
tuple1 = (1,3,5)
tuple2 = ("a","b")
addion = tuple1 + tuple2
print(addion)

#3 -- repetition 
# you can repeat a tuple multiople times using the * operatr
tuple3 = tuple1 * 3
print(tuple3)


#4 -- iteration over tuple 
for_store_in_tuple = ()
for element in tuple3:
   print(element)


