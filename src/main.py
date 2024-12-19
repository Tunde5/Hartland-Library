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

