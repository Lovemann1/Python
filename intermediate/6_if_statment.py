loveman = "lovemann"
name = loveman

if name == loveman:
    print("it workded")
if name == "lovemann":
    print("it not worked")   # difference between if and elif is that each if statement is indepandant 
                                # from every other if statement


number = 10
if number > 8:
    print("greater then 8")
elif number > 6:
    print("grater then 6")
elif number > 4:
    print("greater then 4")
else:
    print("greater then 2")