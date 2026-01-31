contacts = {}

def show_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for name, info in contacts.items():
                print(name, "-", info["phone"])

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            info = contacts[search]
            print("Phone:", info["phone"])
            print("Email:", info["email"])
            print("Address:", info["address"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")
        if name in contacts:
            contacts[name]["phone"] = input("New phone: ")
            contacts[name]["email"] = input("New email: ")
            contacts[name]["address"] = input("New address: ")
            print("Contact updated.")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Exiting Contact Book.")
        break

    else:
        print("Invalid choice.")