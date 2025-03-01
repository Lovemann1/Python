# Question:- let's say you want to classify a number as posiftive negative, or zero and further classify
# postive number as even or odd.

number = int(input("enter a number"))
if number > 0:
    if number %2 == 0:
        print("it is even number")
    else:
        print("it is odd")
elif number< 0:
    print("it is a negtive number")
else:
    print("it is zero")


#           2       conditional expression                 
# syntux = (value_if true if condition else velue if false)
print("positive hai" if(number > 0) else "negitive hai")