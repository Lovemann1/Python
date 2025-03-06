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

    




       