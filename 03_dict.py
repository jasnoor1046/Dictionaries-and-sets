# creating a dictionary
# VARIOUS DICTIONARY METHODS PART 1.
my_dict = dict(name="jasnoor", age="18")

# adding a new element
my_dict["city"] = "New York"

# updating the existing value
my_dict["age"] = 16

# removing elements; use del statement
del my_dict["name"]

# using pop
age = my_dict.pop("age")

print(my_dict)
print("removed age: ", age)
