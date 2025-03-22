# set in  python
#                    characterstics of sets
# 1-- unique values / items 
#2 -- unordered -no  indexing
#3 -- mutable - add or remove elements
# 4 -- since there is no indexing system you can't replace or modify existing elements



#                   set operation
 # ADDING elements
numbers = {1,2,4,6,5}
numbers.add(100)
print(numbers)
numbers.remove(5)
numbers.discard(4)  # difference between remove and discard is if there is no element present in set remove will show 
                    # error

#                   set methods 
# 1 union
set1 = {1,2,3}
set2 = {2,4,5}
print(set1.union(set2))  # combines elements from two set in one set


#2 intersection
print(set1.intersection(set2)) # give you only elemets that is present in both sets

#3 defference 
print(set1.difference(set2))  # give you only elemets that is present only in set1

#4 symmetric difference
print(set1.symmetric_difference(set2)) # element in either side but not in both side

# set Iterations
 # in for loop
numbers = {1,2,3,4,5,6,7}
tem_list = []
for _ in numbers:
    a = _*2
    tem_list.append(a)
print(tem_list)

# donot support while loop

# set compreshesion
squeres = {x**2 for x in range(1,6)}
print(squeres)