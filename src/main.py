# Initialize lists to store data
books = [
    {"BookID": "101", "Title": "Quotations from Chairman Mao Tse-Tung", "Author": "Mao Zedong", "Availability": "Available"},
    {"BookID": "102", "Title": "The Quran", "Author": "Anonymous", "Availability": "Available"},
    {"BookID": "103", "Title": "Xinhua Zidian", "Author": "Wei Jiangong", "Availability": "Available"},
    {"BookID": "104", "Title": "Don Quixote", "Author": "Miguel de Cervantes", "Availability": "Available"},
    {"BookID": "105", "Title": "A Tale of Two Cities", "Author": "Charles Dickens", "Availability": "Available"},
    {"BookID": "106", "Title": "The Book of Mormon", "Author": "Joseph Smith", "Availability": "Available"}
]
# Initialize users list with data
users = [
    {"UserID": "U001", "Name": "Alice Johnson", "Contact": "alice.johnson@example.com"},
    {"UserID": "U002", "Name": "Bob Smith", "Contact": "bob.smith@example.com"},
    {"UserID": "U003", "Name": "Charlie Brown", "Contact": "charlie.brown@example.com"},
    {"UserID": "U004", "Name": "Diana Prince", "Contact": "diana.prince@example.com"},
    {"UserID": "U005", "Name": "Eve Adams", "Contact": "eve.adams@example.com"}
]
# Initialize transactions records (borrow/return)
transactions = [
    {"TransactionID": "T001", "UserID": "U001", "BookID": "101", "Type": "Borrow", "Date": "2024-01-10"},
    {"TransactionID": "T002", "UserID": "U002", "BookID": "102", "Type": "Borrow", "Date": "2024-01-12"},
    {"TransactionID": "T003", "UserID": "U003", "BookID": "103", "Type": "Borrow", "Date": "2024-01-15"},
    {"TransactionID": "T004", "UserID": "U004", "BookID": "104", "Type": "Return", "Date": "2024-01-20"},
    {"TransactionID": "T005", "UserID": "U005", "BookID": "105", "Type": "Borrow", "Date": "2024-01-22"}
]
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
# Manage books
def manage_books():
    print("\nManage Books")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Remove Book")
    print("4. Search Book")
    print("5. Back to Main Menu")
    action = input("Enter your choice: ")

    if action == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        availability = "Available"
        books.append({"BookID": book_id, "Title": title, "Author": author, "Availability": availability})
        print("Book added successfully!")

    elif action == "2":
        book_id = input("Enter Book ID to update: ")
        for book in books:
            if book["BookID"] == book_id:
                book["Title"] = input("Enter new Title: ")
                book["Author"] = input("Enter new Author: ")
                print("Book updated successfully!")
                return
        print("Book not found!")

    elif action == "3":
        book_id = input("Enter Book ID to remove: ")
        books[:] = [book for book in books if book["BookID"] != book_id]
        print("Book removed successfully!")

    elif action == "4":
        search_query = input("Enter Title or Author to search: ").lower()
        results = [book for book in books if search_query in book["Title"].lower() or search_query in book["Author"].lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found!")
if choice == "1":
    manage_books()
    # Manage users
    def manage_users():
        print("\nManage Users")
        print("1. Register User")
        print("2. Update User Info")
        print("3. Remove User")
        print("4. Back to Main Menu")
        action = input("Enter your choice: ")

        if action == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            contact = input("Enter Contact Info: ")
            users.append({"UserID": user_id, "Name": name, "Contact": contact})
            print("User registered successfully!")

        elif action == "2":
            user_id = input("Enter User ID to update: ")
            for user in users:
                if user["UserID"] == user_id:
                    user["Name"] = input("Enter new Name: ")
                    user["Contact"] = input("Enter new Contact Info: ")
                    print("User updated successfully!")
                    return
            print("User not found!")

        elif action == "3":
            user_id = input("Enter User ID to remove: ")
            users[:] = [user for user in users if user["UserID"] != user_id]
            print("User removed successfully!")
if choice == "2":
    manage_users()

    # Borrow/Return books
    def borrow_return_books():
        print("\nBorrow/Return Books")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Back to Main Menu")
        action = input("Enter your choice: ")

        if action == "1":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            for book in books:
                if book["BookID"] == book_id and book["Availability"] == "Available":
                    transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Borrow"})
                    book["Availability"] = "Borrowed"
                    print("Book borrowed successfully!")
                    return
            print("Book not available!")

        elif action == "2":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            for book in books:
                if book["BookID"] == book_id and book["Availability"] == "Borrowed":
                    transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Return"})
                    book["Availability"] = "Available"
                    print("Book returned successfully!")
                    return
            print("Book not found or already available!")
if choice == "3":
    borrow_return_books()


