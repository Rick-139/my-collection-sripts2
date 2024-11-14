import json
import os

def load_contacts(filename):
    """Load contacts from a JSON file."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        return json.load(file)

def save_contacts(filename, contacts):
    """Save contacts to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(contacts, file, indent=4)

def display_contacts(contacts):
    """Display the list of contacts."""
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. Name: {contact['name']}, Phone: {contact['phone']}")

def main():
    filename = 'contacts.json'
    contacts = load_contacts(filename)

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contacts.append({'name': name, 'phone': phone})
            save_contacts(filename, contacts)
            print(f'Contact "{name}" added.')

        elif choice == '2':
            display_contacts(contacts)

        elif choice == '3':
            display_contacts(contacts)
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                if 0 <= index < len(contacts):
                    removed_contact = contacts.pop(index)
                    save_contacts(filename, contacts)
                    print(f'Contact "{removed_contact["name"]}" deleted.')
                else:
                    print("Invalid contact number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
