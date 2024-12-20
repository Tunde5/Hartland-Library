# Add Book, Update Book, Remove Book, Search Book, Borrow Book, Return Book, Register User, Update User, Remove User,

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.functions import display_welcome_message, save_books, manage_books
from src import database

def test_functions():
    print("\n--- Test: Display Welcome Message ---")
    display_welcome_message()

    print("\n--- Test: Add Books ---")
    save_books("1984", "George Orwell")
    save_books("To Kill a Mockingbird", "Harper Lee")

    print("\nCurrent Books in the Library:")
    for book in database.org_books:
        print(book)

# Run app

test_functions()

# Test Add Book, example title Harry Potter
def test_add_book():
    print("\nTesting Add Book...")
    initial_count = len("org_books")

# Run the actual add_book function
def add_book():
    if len("org_books") == ("initial_count") + 1:
        print("Test Passed: Book added successfully.")
    else:
        print("Test Failed: Book was not added.")


def test_update_book():
    print("\nTesting Update Book...")
    add_book()  # First add a book to update
    book_id = "org_books"[-1][("BookID")]
    old_title = "org_books"[-1]["Title"]
    # Run the actual update_book function
    update_book()
    new_title = "org_books"[-1]["Title"]
    if old_title != new_title:
        print("Test Passed: Book updated successfully.")
    else:
        print("Test Failed: Book was not updated.")


def test_remove_book():
    print("\nTesting Remove Book...")
    add_book()  # First add a book to remove
    initial_count = len("org_books")
    # Run the actual remove_book function
    remove_book()
    if len("org_books") == initial_count - 1:
        print("Test Passed: Book removed successfully.")
    else:
        print("Test Failed: Book was not removed.")


def test_search_book():
    print("\nTesting Search Book...")
    add_book()  # Ensure a book is available to search
    # Run the actual search_book function
    search_book()
    # This test requires manual validation by the user for now
    print("Check the search results to verify correctness.")


def test_borrow_book():
    print("\nTesting Borrow Book...")
    add_book()  # Ensure a book exists to borrow

    # Ensure a user exists to borrow the book
    initial_availability = "org_books"[-1]["Availability"]

    # Run the actual borrow_book function
    if "org_books"[-1]["Availability"] == "Borrowed" and initial_availability == "Available":
        print("Test Passed: Book borrowed successfully.")
    else:
        print("Test Failed: Book was not borrowed.")


def test_return_book():
    print("\nTesting Return Book...")
    add_book()  # Ensure a book exists to return
    # Ensure a user exists to return the book
    borrow_book()  # Borrow the book first
    initial_availability = "org_books"[-1]["Availability"]
    return_book()  # Run the actual return_book function
    if "org_books"[-1]["Availability"] == "Available" and initial_availability == "Borrowed":
        print("Test Passed: Book returned successfully.")
    else:
        print("Test Failed: Book was not returned.")


def test_register_user():
    print("\nTesting Register User...")
    initial_count = len("users")
    # Run the actual register_user function
    register_user()
    if len("users") == initial_count + 1:
        print("Test Passed: User registered successfully.")
    else:
        print("Test Failed: User was not registered.")


def test_update_user():
    print("\nTesting Update User...")
    register_user()  # Ensure a user exists to update
    old_name = "users"[-1]["Name"]
    update_user()  # Run the actual update_user function
    new_name = "users"[-1]["Name"]
    if old_name != new_name:
        print("Test Passed: User updated successfully.")
    else:
        print("Test Failed: User was not updated.")


def test_remove_user():
    print("\nTesting Update User...")
    register_user()  # Ensure a user exists to update
    old_name = "users"[-1][("Name")]
    update_user()  # Run the actual update_user function
    new_name = "users"[-1][("Name")]
    if old_name != new_name:
        print("Test Passed: User updated successfully.")
    else:
        print("Test Failed: User was not updated.")


def test_suite():
    print("\nRunning Tests...\n")
    test_add_book()
    test_update_book()
    test_remove_book()
    test_search_book()
    test_borrow_book()
    test_return_book()
    test_register_user()
    test_update_user()
    test_remove_user()
    
    print("\nAll tests completed.")
