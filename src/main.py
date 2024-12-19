# Initialize lists to store data

org_library = {
    "name": "Great Hartland Community Library",
    "opening_times": "Mon-Fri 9-5pm"
}

org_books = [
    {"BookID": "101", "Title": "Quotations from Chairman Mao Tse-Tung", "Author": "Mao Zedong", "Available": "True"},
    {"BookID": "102", "Title": "The Quran", "Author": "Anonymous", "Available": "True"},
    {"BookID": "103", "Title": "Xinhua Zidian", "Author": "Wei Jiangong", "Available": "True"},
    {"BookID": "104", "Title": "Don Quixote", "Author": "Miguel de Cervantes", "Available": "True"},
    {"BookID": "105", "Title": "A Tale of Two Cities", "Author": "Charles Dickens", "Available": "True"},
    {"BookID": "106", "Title": "The Book of Mormon", "Author": "Joseph Smith", "Available": "True"}
]
# Initialize users list with data
org_users = [
    {"UserID": "U001", "Name": "Alice Johnson", "Contact": "alice.johnson@example.com"},
    {"UserID": "U002", "Name": "Bob Smith", "Contact": "bob.smith@example.com"},
    {"UserID": "U003", "Name": "Charlie Brown", "Contact": "charlie.brown@example.com"},
    {"UserID": "U004", "Name": "Diana Prince", "Contact": "diana.prince@example.com"},
    {"UserID": "U005", "Name": "Eve Adams", "Contact": "eve.adams@example.com"}
]
# Initialize transactions records (borrow/return)
org_transactions = [
    {"TransactionID": "T001", "UserID": "U001", "BookID": "101", "Type": "Borrow", "Date": "2024-01-10"},
    {"TransactionID": "T002", "UserID": "U002", "BookID": "102", "Type": "Borrow", "Date": "2024-01-12"},
    {"TransactionID": "T003", "UserID": "U003", "BookID": "103", "Type": "Borrow", "Date": "2024-01-15"},
    {"TransactionID": "T004", "UserID": "U004", "BookID": "104", "Type": "Return", "Date": "2024-01-20"},
    {"TransactionID": "T005", "UserID": "U005", "BookID": "105", "Type": "Borrow", "Date": "2024-01-22"}
]
# Welcome message
def display_welcome_message():
    print("\nWelcome to", org_library["name"] )

    print("\nNote: last book ID is:", org_books[-1]["BookID"] )


# Manage books
def manage_books():
    print("\nManage Books")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Back to Main Menu")

    input_action = input("Enter your choice: ")

    def add_book():
        print("\n--- Add a Book ---")
        book_id = input("Enter BookID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        availability = "Available"
        org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": availability})
        print(f"Book '{title}' added successfully!")

    if input_action == "1":

        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        available = "True"

        # Save book
        # book Id is the last book ID + 1
        book_id = int(org_books[-1]["BookID"]) + 1
        org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": available})
        print("Book added successfully!")

    elif input_action == "2":
        book_id = input("Enter Book ID to update: ")
        for book in org_books:
            if book["BookID"] == book_id:
                book["Title"] = input("Enter new Title: ")
                book["Author"] = input("Enter new Author: ")
                print("Book updated successfully!")
                return
        print("Book not found!")

    elif input_action == "3":
        book_id = input("Enter Book ID to remove: ")
        org_books[:] = [book for book in org_books if book["BookID"] != book_id]
        print("Book removed successfully!")

    elif input_action == "4":
        search_query = input("Enter Title or Author to search: ").lower()
        results = [book for book in org_books if search_query in book["Title"].lower() or search_query in book["Author"].lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found!")


# Manage users
def manage_users():
    print("\nManage Users")
    print("1. Register User")
    print("2. Update User Info")
    print("3. Remove User")
    print("4. Back to Main Menu")
    input_action_users = input("Enter your choice: ")

    if input_action_users == "1":
        user_id = input("Enter User ID: ")
        name = input("Enter User Name: ")
        contact = input("Enter Contact Info: ")
        org_users.append({"UserID": user_id, "Name": name, "Contact": contact})
        print("User registered successfully!")

    elif input_action_users == "2":
        user_id = input("Enter User ID to update: ")
        for user in org_users:
            if user["UserID"] == user_id:
                user["Name"] = input("Enter new Name: ")
                user["Contact"] = input("Enter new Contact Info: ")
                print("User updated successfully!")
                return
        print("User not found!")

    elif input_action_users == "3":
        user_id = input("Enter User ID to remove: ")
        org_users[:] = [user for user in org_users if user["UserID"] != user_id]
        print("User removed successfully!")

# Borrow/Return books
def borrow_return_books():
    print("\nBorrow/Return Books")
    print("1. Borrow Book")
    print("2. Return Book")
    print("3. Back to Main Menu")
    input_action_books = input("Enter your choice: ")

    if input_action_books == "1":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")
        for book in org_books:
            if book["BookID"] == book_id and book["Available"] == "True":
                org_transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Borrow"})
                book["Available"] = "False"
                print("Book borrowed successfully!")
                return
        print("Book not available!")

    elif input_action_books == "2":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")
        for book in org_books:
            if book["BookID"] == book_id and book["Available"] == "False":
                org_transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Return"})
                book["Available"] = "True"
                print("Book returned successfully!")
                return
        print("Book not found or not available!")
    if input_action_books == "3":
        borrow_return_books()



# Main program loop
def main():

    display_welcome_message()

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
                    manage_books()  # Call the manage_books function
                elif input_choice == "2":
                    manage_users()  # Call the manage_users function
                elif input_choice == "3":
                    borrow_return_books()  # Call the borrow/return function
                elif input_choice == "4":
                    print("Thank you for using the library system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")

        main_menu()

main()
