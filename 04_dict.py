# VARIOUS DICTIONARY METHODS PART 2.
# dictionary comprehension
squared = {x: x * x for x in range(6)}
print(squared)

# merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)

# copy function
my_dict_copy = dict1.copy()
print(my_dict_copy)
