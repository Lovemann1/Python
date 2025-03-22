# what are function arguments
# arguments are the values that are passed into a fuction when it's called.
# A functon had 2 parameters, you must provide 2 arguments when calling it.

def greetings(name):
    return("hello, " + name + "!")

print(greetings("madhav"))

# Types of function arguments 
# Python support various types of arguments that can be passed at the time of the functon call 
# -- required arguments ( single\ multiple arguments)
# --default arguments(named argumets)
# --keyword argumetys(named argumets)
# --arbitary argumets(variable-length argumets*args and ** kwargs)


# required arguments
def greeting(name):  #name is a parameter
    print(name)
greeting("you have to give some argumet here ")

# default arguments
def my_name(name = "loveman"):
    print("my name is ", name)
my_name()
my_name("rohit")

# keyword arguments 
# when calling a function, you can specify arguments by the parameter name.
# These are called keyword argumetns and can be given in any order

def divide(a,b):
    return(a/b)

result = divide(100,20)   # here i didnot use the parameter name so python use the order to identify parameter 
print(result)

def divide_by_position(a,b):
    return(a/b)

result_by_position = divide(b = 100, a = 20) # here i used the parameter so python don't use positon for to  find right argument
print(result_by_position)


# arbitaray positonal arguments(* args):
# if you are not sure how many arguments will passed, use * args to accept andy number of positional arguments.
# purpose: allows you to poss a variable number fo positional arguments.
# ---type: The arguments are stored as a tuple.---
# Usage: use when you want to pass multiple values that are accessed by position.

def add_numbers(*args):
    return sum(args)
op = add_numbers(1,2,5,6)
print(op)

