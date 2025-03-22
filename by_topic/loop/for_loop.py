#for loop in python is used to iterate over a sequence (such as a list, tuple, ditionary, set, or string) and exetute
# a block of code for each element in that sequence.


#syntax :
#    *for* variable *in* seqence

#making exponation function
def raise_to_power(base_num,pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result

print(raise_to_power(3,4))

number = (10,20,30)
for num in number:
    print(num)
print(num)


language = "python"
for x in language:
    print(x)
# pass in for loop
for i in range(6):
    pass


for c in range(11):
    if c == 5:
        pass
    else:
        print(c)

for c in range(11):
    if c == 5:
        break
    print(c)



# makeing delebrately infinity loop
# n = 0
# while n < 1 :
#     n = int(input("enter a number"))
# print(n)


# list in for loop 

students = ["hermione", "harry" ,"Ron"]
print(students)
for student in students:
    print(student)

# dict in for loop

students = [
    {"name":"hermione", "house":"gryffindor","patronus":"otter"},
    {"name":"harry","house":"gryffindor","patronus":"stag"},
    {"name":"ron","house":"gryffindor","patronus":"jack Russell terrir"},
    {"name":"draco","house":"slytherin","patronus": None}
]

for student in (students):
    print(student["name"])

a = students[0]
print(a)
