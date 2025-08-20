import json
import os

File_Name = os.path.join(os.path.dirname(__file__), "contacts.json")

def load_contacts():
    if not os.path.exists(File_Name):
        return []
    else:
        with open(File_Name, 'r') as file:
            return json.load(file)

def save_contacts(contacts):
    with open(File_Name, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact Added Successfully")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact['name'].strip().lower() == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()
    for contact in contacts:
        if contact['name'].strip().lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact Deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()

    while True:
        print("|-------------------------|")
        print("|--- Contact Book Menu ---|")
        print("|-------------------------|")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(contacts)
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
