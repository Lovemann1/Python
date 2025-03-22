# print while in same line
print("hello", sep = "*", end="&&" )
i = 1
while i < 4:
    i = i +1
    print(f"hello {i}" , sep = "_&&&_", end = "**")


# star pattern
n = 5
for i in range(1, n +1): #1, 2
    for j in range(1,i+1):
        print("*",end= "-")
    print()

# facrorial of (n)
def factorial(n):
    result = 1
    while n> 0:
        result = result*n
        n = n - 1
        #print(result)
    return result

print(factorial(5))
#4 count vowels in a string
my_string = "zop"
# vowels = "aeiou"
count = 0
for char in my_string:
    if char.lower() in ("a","e","i","o","u"):
        count = count +1
    
print("vowels count is ", count)

#5 find the longest word in a string
string = "python by Rishabh Mishra"
words = string.split()
print(words)
longest_word = ""
for w in words:
    if len(w) > len(longest_word):
        longest_word = w
print(len(longest_word))

