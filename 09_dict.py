def extract_unique_values(dicts):
    unique_values = set()
    for d in dicts:
        for value in d.values():
            unique_values.add(value)
    return list(unique_values)


def input_dictionaries():
    dicts = []
    while True:
        user_input = input("Enter a dictionary : ")
        if user_input.lower() == "done":
            break
        try:
            user_dict = eval(user_input)
            if isinstance(user_dict, dict):
                dicts.append(user_dict)
            else:
                print("Please enter a valid dictionary.")
        except:
            print("Please enter a valid dictionary format.")
    return dicts


user_dicts = input_dictionaries()

unique_values = extract_unique_values(user_dicts)
print("Unique Values:", unique_values)
