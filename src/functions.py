import database 

# Welcome message

def display_welcome_message():
    print("\nWelcome to", database.org_library["name"])
    if database.org_books:
        print("\nNote: Last book ID is:", database.org_books[-1]["BookID"])
    else:
        print("\nNo books in the library yet.")


# Save a New Book
def save_books(title, author, available="True"):
    book_id = str(int(database.org_books[-1]["BookID"]) + 1) if database.org_books else "1"
    database.org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": available})
    print(f"Book '{title}' added successfully with ID: {book_id}")


# Manage Books Menu
def manage_books():
    while True:
        print("\nManage Books")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Search Book")
        print("5. Back to Main Menu")
        input_action = input("Enter your choice: ")

        if input_action == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            save_books(title, author)

        elif input_action == "2":
            book_id = input("Enter Book ID to update: ")
            for book in database.org_books:
                if book["BookID"] == book_id:
                    book["Title"] = input("Enter new Title: ")
                    book["Author"] = input("Enter new Author: ")
                    print("Book updated successfully!")
                    break
            else:
                print("Book not found!")

        elif input_action == "3":
            book_id = input("Enter Book ID to remove: ")
            initial_count = len(database.org_books)
            database.org_books[:] = [book for book in database.org_books if book["BookID"] != book_id]
            if len(database.org_books) < initial_count:
                print("Book removed successfully!")
            else:
                print("Book not found!")

        elif input_action == "4":
            search_query = input("Enter Title or Author to search: ").lower()
            results = [
                book for book in database.org_books
                if search_query in book["Title"].lower() or search_query in book["Author"].lower()
            ]
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found!")

        elif input_action == "5":
            break

        else:
            print("Invalid choice. Please try again.")


# Manage Users Menu
def manage_users():
    while True:
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
                    break
            else:
                print("User not found!")

        elif input_action_users == "3":
            user_id = input("Enter User ID to remove: ")
            initial_count = len(database.org_users)
            database.org_users[:] = [user for user in database.org_users if user["UserID"] != user_id]
            if len(database.org_users) < initial_count:
                print("User removed successfully!")
            else:
                print("User not found!")

        elif input_action_users == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Borrow/Return Books Menu
def borrow_return_books():
    while True:
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
                    break
            else:
                print("Book not available or already borrowed!")

        elif input_action_books == "2":
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID: ")
            for book in database.org_books:
                if book["BookID"] == book_id and book["Available"] == "False":
                    database.org_transactions.append({"UserID": user_id, "BookID": book_id, "Type": "Return"})
                    book["Available"] = "True"
                    print("Book returned successfully!")
                    break
            else:
                print("Book not found or already returned!")

        elif input_action_books == "3":
            break

        else:
            print("Invalid choice. Please try again.")


