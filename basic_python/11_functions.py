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

def greet(a,b):
     print(f"hi {a} and hlo {b} ")
     print("another line")

greet("ashish","pankaj")
greet("nisha","depika")
greet(23,34)


# function are of two type
# function that perform the task
def function_for_sanj(p,q):
     print(q+p)
function_for_sanj("not","do")

# function that return value
def calculatoradd(*numbers):
     return sum(numbers)
var = calculatoradd(2,6,55,  34)
print(var)
     
