FILENAME = "data.txt"

def load_contacts():
    pass

def show_contacts():
    pass

def add_contact():
    pass

def delete_contact():
    pass

def edit_contact():
    pass


def main():
    contacts = load_contacts()
    while True:
        print("\n--- Contact Manager ---")
        print("1. Show contacts")
        print("2. Add contact")
        print("3. Delete contact")
        print("4. Update a contact")
        print("5. Exit")

        choice = input("Enter your choice by number: ")

        if choice == "1":
            show_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
        print("5. Exit")

main()
