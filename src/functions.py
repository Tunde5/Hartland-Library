import database 

# Welcome message
def display_welcome_message():
    print("\nWelcome to", database.org_library["name"] )

    print("\nNote: last book ID is:", database.org_books[-1]["BookID"] )


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
        database.org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": availability})
        print(f"Book '{title}' added successfully!")

    if input_action == "1":

        title = input("Enter Book Title: ")
        author = input("Enter Author: ")
        available = "True"

        # Save book
        # book Id is the last book ID + 1
        book_id = int(database.org_books[-1]["BookID"]) + 1
        database.org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": available})
        print("Book added successfully!")

    elif input_action == "2":
        book_id = input("Enter Book ID to update: ")
        for book in database.org_books:
            if book["BookID"] == book_id:
                book["Title"] = input("Enter new Title: ")
                book["Author"] = input("Enter new Author: ")
                print("Book updated successfully!")
                return
        print("Book not found!")

    elif input_action == "3":
        book_id = input("Enter Book ID to remove: ")
        database.org_books[:] = [book for book in database.org_books if book["BookID"] != book_id]
        print("Book removed successfully!")

    elif input_action == "4":
        search_query = input("Enter Title or Author to search: ").lower()
        results = [book for book in database.org_books if search_query in book["Title"].lower() or search_query in book["Author"].lower()]
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
        database.org_users.append({"UserID": user_id, "Name": name, "Contact": contact})
        print("User registered successfully!")

    elif input_action_users == "2":
        user_id = input("Enter User ID to update: ")
        for user in database.org_users:
            if user["UserID"] == user_id:
                user["Name"] = input("Enter new Name: ")
                user["Contact"] = input("Enter new Contact Info: ")
                print("User updated successfully!")
                return
        print("User not found!")

    elif input_action_users == "3":
        user_id = input("Enter User ID to remove: ")
        database.org_users[:] = [user for user in database.org_users if user["UserID"] != user_id]
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
        for book in database.org_books:
            if book["BookID"] == book_id and book["Available"] == "True":
                database.org_transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Borrow"})
                book["Available"] = "False"
                print("Book borrowed successfully!")
                return
        print("Book not available!")

    elif input_action_books == "2":
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID: ")
        for book in database.org_books:
            if book["BookID"] == book_id and book["Available"] == "False":
                database.org_transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Return"})
                book["Available"] = "True"
                print("Book returned successfully!")
                return
        print("Book not found or not available!")
    if input_action_books == "3":
        borrow_return_books()

