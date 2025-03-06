# string in Python
# string is a sequence of characters. In python, string are enclosed within single('')or duble("") quotation marks.
print("hello world")


# formatted string
#  a formatted string in python a way to insert varialbes or expressions
#  inside a string. IT allows you to format the output in a readable and controlled way.
# there are multiple way to format a strings in Python

#_1 old style formatting(% operator)
#2 str.format() method
#3 F-strng(formatted string literals)


#1 
#syntex: "string % value"

#example 
name = "madhav"
age = 24
print("my name is %s and I'm %d" % (name, age))

#2 
#syntex:  str.format() method

name2 = "madhav2"
age2 = 25
print("my name is {} and I'm {}" .format(name2,age2))
# you can referance variables by index or keyword
print("my name is {1} and I'm {1}".format(name2, age2))

# you can referance variables directly inside
print("my name is {name2} my age is {age2}".format(name2 = "loveman", age2 = 22))

#3 
#syntax: f"string{variable}
name3 = "madhav3"
age4 = 44

print(f"my name is {name3 + "aa"} my age is {age4}")


#4
# escape characters 
# \n 
print("hello\n world")
print("hello\t world")  # t for tap 




name = "bro code"
print(len(name))      # this is length function
print(name.find("c")) # will find the character 
print(name.index("c")) # will find the character
print(name.upper())   # will make it upper case
print("bro it is hard very hard".capitalize()) # make capitalize
name = "canged bro code"
print(name.replace("c","C"))  # replaced one letter with another


#Qu1
# 1. username is no more then 12 world
# 2. username must not contain spaces
# 3. username must not contain digite

username = input("enter your username")
if len(username)> 12 or username.find("_"):
    print("username can't be more then 12 letter and spaceses")
else:
    print("welcome ",username)