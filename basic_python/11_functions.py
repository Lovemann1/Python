# function is block of code that performs a specific task. you can use it 
# whenever you want by calling its name, whick save you from writing the same code multiple times
# benefits of using function: increase code readablity & resuablity.
# basic concepts:
# -- create function use the def keyword to define a function
# -- call function : use the functin's name followed by () to run
# -- paramater : the variable listed inside paretheses in function
# -- argument : the actual value  you pass to function when you


# type of functon 
# built in function
# -- these are standard functions in python that are available to use.
# -- examples: print(), input(), type(), sum(), max(), etc
# user - defined functon:
#user-defined function
#-- we can create our own functions based on our requerment
#-- example: create your own funciton---

#function to add 2 numbers & print result
# def add2number(a,b):    # these are the parameter
#     result = a + b      
#     print(" the result of adding a and b ", result)
# add2number(4,5)  # these are arguments

def add2(a,b):
     return a + b 
result = add2(3,5)
print(result)

