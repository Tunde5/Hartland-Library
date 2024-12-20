import database 

# Display main menu
def display_main_menu():

    print("\nMain Menu")
    print("0. Exit")
    print("1. Manage Books")
    print("2. Manage Users")
    print("3. Borrow/Return Books")
    print("4. Show library statistics")


# Welcome message
def display_welcome_message():

    print("\nWelcome to", database.org_library["name"])
    print("Serving our community with a diverse collection of books.\n")


# Print library statistics
def library_statistics():

    print("\nLibrary statistics:")
    print("Number of books:", len(database.org_books))
    print("Number of users:", len(database.org_users))
    print("Number of transactions:", len(database.org_transactions))
    print("Last book ID is:", database.org_books[-1]["BookID"])

# Save a New Book
def save_books(title, author, available="True"):
    if len(database.org_books):
        book_id = str(int(database.org_books[-1]["BookID"]) + 1)
    else:
        book_id = 1
    database.org_books.append({"BookID": book_id, "Title": title, "Author": author, "Available": available})
    print(f"Book '{title}' added successfully with ID: {book_id}")

# Manage Books Menu
def manage_books():
    while True:
        print("\nManage Books")
        print("0. Back to Main Menu")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Search Book")
        input_action = input("Enter your choice: ")

        if input_action == "1":
            # Add book
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            save_books(title, author)

        elif input_action == "2":
            # Update book
            book_id = input("Enter Book ID: ")
            for book in database.org_books:
                if book["BookID"] == book_id:
                    book["Title"] = input("Enter new Title: ")
                    book["Author"] = input("Enter new Author: ")
                    print("Book updated successfully!")
                    break
            else:
                print("Book not found!")

        elif input_action == "3":
            # Remove book
            book_id = input("Enter Book ID: ")
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

        elif input_action == "0":
            break

        else:
            print("Invalid choice. Please try again.")

# Manage Users Menu
def manage_users():
    while True:
        print("\nManage Users")
        print("0. Back to Main Menu")
        print("1. Register User")
        print("2. Update User Info")
        print("3. Remove User")

        input_action_users = input("Enter your choice: ")

        if input_action_users == "1":

            # Register user

            name = input("Enter Name: ")
            email = input("Enter Email Address: ")

            # save user

            if len(database.org_users):
                user_id = str(int(database.org_users[-1]["UserID"]) + 1)
            else:
                user_id = 1

            database.org_users.append({"UserID": user_id, "Name": name, "Email": email})
            print("User registered successfully! User ID is ", user_id)

        elif input_action_users == "2":

            # Update user

            user_id = input("Enter User ID: ")
            for user in database.org_users:
                if user["UserID"] == user_id:
                    user["Name"] = input("Enter Name: ")
                    user["Email"] = input("Enter Email Address: ")
                    print("User updated successfully!")
                    break
            else:
                print("User not found! Try again!")

        elif input_action_users == "3":

            # Remove user

            user_id = input("Enter User ID: ")

            initial_count = len(database.org_users)

            database.org_users[:] = [user for user in database.org_users if user["UserID"] != user_id]

            if len(database.org_users) < initial_count:
                print("User removed successfully!")
            else:
                print("User not found! Try again!")

        elif input_action_users == "0":
            break

        else:
            print("Invalid choice. Please try again.")

# Borrow/Return Books Menu
def borrow_return_books():
    while True:
        print("\nBorrow/Return Books")
        print("0. Back to Main Menu")
        print("1. Borrow Book")
        print("2. Return Book")

        input_action_books = input("Enter your choice: ")

        if input_action_books == "1":
            # Borrow book
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
            # Return book
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

        elif input_action_books == "0":
            break

        else:
            print("Invalid choice. Please try again.")


