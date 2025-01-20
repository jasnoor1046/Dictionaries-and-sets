# to print a merged dictionary along with the sum of duplictate keys.
import ast


def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    # this creates a new dictionary which is a copy of dict1.This ensures the original dict1 remains same.

    for key, value in dict2.items():
        # this will goes through the key value pair in dict2.

        if key in merged:
            merged[key] += value

        else:
            merged[key] = value
            # if a key from dict already exists in merged, the values are summed; if the key does not exist
            # it's simply added to merged with its value from dict2
    return merged


# function to take dictionary from the user.
def input_dictionary(prompt):
    user_input = input(prompt)
    try:
        user_dict = ast.literal_eval(user_input)
        if isinstance(user_dict, dict):
            return user_dict
        else:
            raise ValueError("Input is not a dictionary.")
    except (ValueError, SyntaxError):
        print("Invalid input format. Please enter a valid dictionary.")
        return input_dictionary(prompt)


dict1 = input_dictionary("Enter first dictionary : ")
dict2 = input_dictionary("Enter second dictionary: ")

merged_dict = merge_dictionaries(dict1, dict2)

print("Merged Dictionary:", merged_dict)
