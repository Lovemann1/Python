
# Best meathod of doing 

math = int(input("inter math no."))
physics = int(input("inter phy. no"))
chemistry = int(input("inter chem. no"))

if (math >= 65 and
    physics >= 55 and
    chemistry >= 50 and
    (math + physics + chemistry >= 180 or math + physics >= 140)):
    print("you are eligible")
else:
    print("you are not eligible")





# second meathod of doing

math = int(input("enter math no,"))
if math >= 64:
    physics = int(input("enter physics no."))
    if physics >= 55:
        chemistry = int(input("enter chemistry no"))
        if chemistry >= 50:
            print("you are entered sessesfully")
        
        else:
            print("you have low no in chemisty")
    else :
        print("you have low no in physics")
else:
    print("your math no. is low")

    

# third mathod of doing

math = int(input("inter math no."))
physics = int(input("inter phy. no"))
chemistry = int(input("inter chem. no"))

if math >= 65:
    if physics >= 55:
        if chemistry >= 50:
            if math + physics + chemistry >= 180 or math + physics >= 140:
                print("congratualtion you are selected")
            
            else:
                print("your total no. is not adding 180")
        else:
            print("you chemistry no. is low")
    else:
        print("your physics no. is low")
else:
    print("your math no. is low ")
