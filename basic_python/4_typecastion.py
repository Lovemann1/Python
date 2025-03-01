#/ what is typecasting 
# process of converting a value from one data type to another.
# can be usful when you are proformin operations between different types of data or
# when you need to format data in a specific way. python has several built-in function for type costing:

# int() : converts a value to an interger 
a = "1"
print (a)
b = 2 



c = int(a)
print(b+c)
# or you can use like this 
print(b+int(a))


# implicit type casting
# it is automaticly by python 
var1 = 10
var2 = 15.5
print(var1 + var2)
var3 = var1 + var2
print(type(var3))

#explicit type casting
# aslo know as typecosting is perform manually by the programmar using built in function 
# ex. int(var._name) it will convert any datatype to int.
int_1 = 101
changed_datatype = str(int_1)
print(type(changed_datatype))





