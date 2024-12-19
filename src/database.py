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