# function is a collection of code with performs a specific task. 
# so i can take a bunch of line of code that do anything and 
# i can put that inside a function and then when i wanna to do that task or do that one thing 
# i can call that 

# create a function tha say hi to the person
input_name = input()
def greeting():
    print("hello",input_name)
greeting()



# giving addition information to the functions 
# i.e. parameter

def say_hi(name,age = 70):
    print(f"hi {name} who is {age} year old")

say_hi("mike",29)
say_hi("ravi",25)
say_hi(input_name)
