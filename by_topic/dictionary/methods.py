#add or modify item  use assign-operator '=' to add/modify in a dictionary.
# adding a new key value pair

studnet_ = dict([("name","madhav"), ("age",20), ("grade", "A")])
studnet_["email"] = "madhav@example.com"

# modify on existing value
studnet_["age"] = 25



#2 remove item : use del or .pop() to remove item form a dictionary

# remove with pop() and store the removed value
#email = studnet_.pop('email')


# method in dectionary
# 1 keys 
print(studnet_.keys()) 

# 2 values
print(studnet_.values())


# 3 items
print(studnet_.items())

# get
print(studnet_.get('name',"not have this value"))



