# python program to create a single calculator
#   steps
#   functions for operations
#  user input
# print result



# function to add two numbers

def add(num1,num2):
    return (num1 + num2)

# function to sub. two numbers
def sub(num1,num2):
    return(num1 - num2)

# function to mul. two numbers
def multiply(num1,num2):
    return(num1 * num2)

# function to divide. two numbers
def devide(num1,num2):
    return(num1 / num2)

# function to average two numbers
def avg(num1,num2):
    return(num1 + num2)/2


#  user input
print("select a operation: \n" \
      "1. Addition\n"\
        "2. substraction\n"\
        "3. multiplication\n"\
        "4. devision\n"\
        "5. average\n")

select = int(input("select a operaton from 1, to 5 :- "))
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))


# print the result 
if select ==1:
    print("sum of these numbers is", add(number1,number2))
elif select ==2:
    print("sub of these numbers is ", sub(number1,number2))
elif select ==3:
    print("multiply of these numbers is ", multiply(number1,number2))
elif select ==4:
    print("divide of these numbers is ", devide(number1,number2))
elif select ==5:
    print("avg of these numbers is ", avg(number1,number2))
else:
    print("invalid_oprater")




