# to make a phonebook dictionary.
def phonebook():
    phonebook = {}

    while True:
        print(
            "1.Add contact\n2.Update contact\n3.Delete contact\n4.Search contact\n5.Exit"
        )
        choice = int(input("choose an option: "))

        if choice == 1:
            name = input("Enter name: ")
            number = input("Enter number: ")
            phonebook[name] = number
            print(f"Added {name}:{number}")

        elif choice == 2:
            name = input("Enter a name to update: ")
            if name in phonebook:
                number = input("enter new number: ")

                phonebook[name] = number
                print(f"Updated {name}:{number}")
            else:
                print(f"{name} not found!")

        elif choice == 3:
            name = input("Enter the name to be deleted: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted {name}")
            else:
                print(f"({name} is not found: )")

        elif choice == 4:
            name = input("Enter the name to be searched: ")
            if name in phonebook:
                print(f"{name}:{phonebook[name]}")
            else:
                print(f"{name} not found")

        elif choice == 5:
            break

        else:
            print("Invalid option")


phonebook()
