# inventory mangement system: this will help in storing item details and their quantities in a dictionary
def manage_inventory():
    inventory = {}

    while True:
        print("\nMenu:")
        print("1.Add Item")
        print("2.Update Inventory")
        print("3.Dispaly Inventory")
        print("4.Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            item = input("Enter item name: ")
            quantity = int(input("Enter qauntity: "))
            inventory[item] = quantity
            print(f"Added {quantity} {item}.")

        elif choice == "2":
            item = input("Enter item's name: ")
            if item in inventory:
                quantity = int(input("Enter new quantity:"))
                inventory[item] = quantity
                print(f"Updated {item} to {quantity}: ")

            else:
                print(f"Item {item} not found in inventory")

        elif choice == "3":
            print("\nCurrent Inventory: ")
            for item, quantity in inventory.items():
                # it is used to iterate over all key value pairs in the dictionary, it allows us to access;
                # both item and name and their quantities to display,processing and other operations

                print(f"{item}:{quantity}")

        elif choice == "4":  # to exit the programme
            break
        else:
            print("Invalid choice please try again:")


manage_inventory()
