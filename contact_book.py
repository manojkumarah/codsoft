contacts = {}

def add_contact():
    name = input("Enter name: ").title()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['Phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ").title()
    found = False
    for name, info in contacts.items():
        if search == name or search == info["Phone"]:
            print("\nContact Found:")
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Address: {info['Address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").title()
    if name in contacts:
        print("Leave field blank if you don’t want to change it.")
        phone = input("New phone number: ") or contacts[name]["Phone"]
        email = input("New email: ") or contacts[name]["Email"]
        address = input("New address: ") or contacts[name]["Address"]
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").title()
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found.")

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exit")
        break
    else:
        print("Invalid.")
