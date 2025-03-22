# some methods are following
#1 append
frute = ["apple", "banana", "charry"]
frute.append(34345)
print(frute)

#2 extend
frute = ["apple","orange"]
more_frute = ["cherry", "date"]
frute.extend(more_frute)
print(frute)

#3 insert 
frute = ["apple","orange"]
frute.insert(1,["mango"])
print(frute)


#4 remove
#5 clear
frute = ["banana","apple", "charry","banana"]
frute.clear()  # empty list
print(frute)

#6 finding index
frute = ["banana","apple", "charry","banana"]
index = frute.index("banana",1)
print(index)

#7 count element
element = frute.count("charry")
print(element)

#8 reverce list
frute.reverse()
print(frute)

#9 sorting list
number = [2,35,75,44,2,54,99,32,44,33,74,7]
number.sort()
print(number)

        # sorting list in descending order 
number.sort(reverse = True)
print(number)

        # key in sorting                        note: in key you can add any formula or function
my_list = [ [23,34],[34,55,34],[3],[34345]]
my_list.sort(key=sum)
print(my_list)

# 10 pop with index value
number = [10,23,45,67,88,1,99]
remove_1 = number.pop(-2)
print(remove_1)
print(number)

# 11 copy list
frute = ["banana","apple", "charry","banana"]
frute_copy = frute.copy()
frute_copy.append("orenge")
print(frute_copy)
print(frute)

# why do so because if you assign it by = and after that if you make change in one list it will 
# also change another list also

frute = ["banana","apple", "charry","banana"]
frute_copy = frute
frute_copy.append("orenge")
print(frute_copy)
print(frute)
