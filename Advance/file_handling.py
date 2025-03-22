'so i can write this like that'
# file handling in python
# it had four steps
#   1- opening the file
#   2- reading the file
#   3- writing to a file
#   4- Closing the file

file = open('C:\Python_main\exaple.txt', 'r')
content = file.read()
print(content)
file.close

file = open('example2.txt', 'w')
file.write("namaste! will it work")
file.close()             