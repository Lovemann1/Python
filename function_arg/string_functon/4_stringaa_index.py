# string indexing
# you can access individual characters in a string using their index. python uses zero-based indexing
# ---index: position if the character
# syntax string[index_value]

name = "loveman"
print(name[2]) # give you the 3rd number 

print(name[-5]) # it will give you the last 5th letter


# string slicing 
# slicing in python is a feature that enales acessing parts of the sequence
# string slicing allows you to get subset of charcters from a string using a spercified range of indices.
# string[start : and : step]
print(name[2:7])
print(name[1:6:2])
print(name[-1:-6:2])

# to reverce slicing
print(name[::-1])
