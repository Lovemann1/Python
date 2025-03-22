# create a list of squeres by your own
#syntex:
# list_name = [expressions for item in iterable if condition]

# create a list of squeres
squares = [x**2 for x in range (1,6)]
print(squares)




even_list = [x for x in range (1,20) if x%2 ==0]
print(even_list)

# apply function to each element of a list
frutes = ["apple","banana", "mango", "charry"]
for frute in frutes:
    a = (frute.upper())



def fun_(list_):
    result = []
    for item in list_:
        
        for inside_a in item:
            result.append(inside_a)
    return[result]



print(fun_([[1,2],[3,4],[5,6]]))


    