# Initialize lists to store data
books = []         # List to store book details as dictionaries
users = []         # List to store user details as dictionaries
transactions = []  # List to store transaction records (borrow/return)
# Welcome message
def display_welcome_message():
    print("Welcome to the Great Hartland Community Library!")
    print("Serving our community with a diverse collection of books.\n")

# Display main menu
def display_main_menu():
    print("\nMain Menu")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Borrow/Return Books")
    print("4. Exit")
    return input("Enter your choice: ")

# Main program loop
def main():
    display_welcome_message()
    while True:
        choice = display_main_menu()
        if choice == "4":
            print("Thank you for using the Great Hartland Community Library. Goodbye!")
            break
        else:
            print("Feature not implemented yet!")

if __name__ == "__main__":
    main()
