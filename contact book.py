contacts = []

def display_menu():
    """
    Display the menu for the contact book application.
    """
    print("\nContact Book Menu")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Display all contacts")
    print("6. Exit")

def add_contact():
    """
    Add a new contact to the contacts list.
    """
    name = input("Enter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    contact = {"Name": name, "Email": email, "Phone": phone}
    contacts.append(contact)
    print("Contact added successfully!")

def search_contact():
    """
    Search for a contact by name or email.
    """
    search_term = input("Enter the name or email of the contact to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact["Name"].lower() or search_term in contact["Email"].lower()]

    if found_contacts:
        print("\nMatching contacts found:")
        for contact in found_contacts:
            print(f"Name: {contact['Name']}\nEmail: {contact['Email']}\nPhone: {contact['Phone']}\n-------------------")
    else:
        print("No matching contacts found.")

def update_contact():
    """
    Update an existing contact's details.
    """
    name = input("Enter the name of the contact to update: ").lower()
    found_contact = next((contact for contact in contacts if contact["Name"].lower() == name), None)

    if found_contact:
        print("Contact found. Enter new details:")
        found_contact["Name"] = input("Enter the new name: ")
        found_contact["Email"] = input("Enter the new email: ")
        found_contact["Phone"] = input("Enter the new phone number: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    """
    Delete a contact from the contacts list.
    """
    name = input("Enter the name of the contact to delete: ").lower()
    found_contact = next((contact for contact in contacts if contact["Name"].lower() == name), None)

    if found_contact:
        contacts.remove(found_contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_all_contacts():
    """
    Display all contacts stored in the contacts list.
    """
    if contacts:
        print("\nAll Contacts:")
        for contact in contacts:
            print(f"Name: {contact['Name']}\nEmail: {contact['Email']}\nPhone: {contact['Phone']}\n-------------------")
    else:
        print("No contacts found.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_all_contacts()
    elif choice == "6":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")1
    