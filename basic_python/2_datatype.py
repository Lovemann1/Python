# data type in python 
#1. numaric: Integer, Float, Complex.
#2. Sequence: string, List, Tuple.
#3. Dictionary
#4. set
#5. boolean 
#6. Binary: bytes, Bytearray, Memory


#datatype = 1
a = "1"
b = "1"
print(a+b)
print(type(a)) # this is how we check datatype
a1 = 1 # datatype is integer
a2 = 1.5 # datatype is flot
print(type(a2))
a3 = complex(3,5)
print(type(a3))


# datatype = 2
b1 = "loveman" # datatype is string
b2 = [1,2, b1, "b1 was a another variable added in the list"] # datatype is list
print(b2)
print(type(b2))
b3 = (1,2, b1, "b1 was a another variable added in the list") # dataype is tuple
print(type(b3))


# datatype = 3 
# dictionary it has two always two values always
# (key, value)
my_dictionary = {"name": "Loveman", "age" : 22, "city" : "hisar"}
print(type(my_dictionary))


# datatype = 4 
# sets 
my_sets ={1,2, b1, "b1 was a another variable added in the list"}
print(my_sets)
print(type(my_sets))


# datatype = 5 
# boolean 
bool1 = True
bool2 = False
print(type(bool2))

#datatype = 6
#  binary, bytearray, memoryview 
byte1 = b"madhav"
print(type(byte1))