# program to print a dictionary by taking values from the user.
def get_user_input():
    user_dict = {}
    print("Enter the key value pairs: ")

    while True:
        # this loop continues to prompt user to enter keys and values.
        key = input("Enter key: ")
        if key.lower() == "exit":
            break
        value = input("Enter value: ")
        if value.lower() == "exit":
            break
        user_dict[key] = value

    return user_dict


user_dict = get_user_input()
print("user Dictionary: ", user_dict)
