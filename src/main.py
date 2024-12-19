
import functions

# Main program loop
def main():

    functions.display_welcome_message()

    while True:

        def main_menu():
            while True:
                print("\nMain Menu")
                print("1. Manage Books")
                print("2. Manage Users")
                print("3. Borrow/Return Books")
                print("4. Exit")
                input_choice = input("Enter your choice: ")

                if input_choice == "1":
                    functions.manage_books()  # Call the manage_books function
                elif input_choice == "2":
                    functions.manage_users()  # Call the manage_users function
                elif input_choice == "3":
                    functions.borrow_return_books()  # Call the borrow/return function
                elif input_choice == "4":
                    print("Thank you for using the library system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        main_menu()

main()
