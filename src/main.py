import functions

functions.display_welcome_message()

while True:
    functions.display_main_menu()

    input_choice = input("Enter your choice: ")

    match input_choice:
        case "0":
            print("Thank you for using the library system. Goodbye!")
            break
        case "1":
            functions.manage_books()
        case "2":
            functions.manage_users()
        case "3":
            functions.borrow_return_books()
        case "4":
            functions.library_statistics()

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            print("Invalid choice. Please try again.")
