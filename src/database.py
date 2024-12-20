org_library = {
    "name": "Great Hartland Community Library",
    "opening_times": "Mon-Fri 9-5pm"
}

org_books = [
    {"BookID": "1", "Title": "Quotations from Chairman Mao Tse-Tung", "Author": "Mao Zedong", "Available": "True"},
    {"BookID": "2", "Title": "The Quran", "Author": "Anonymous", "Available": "True"},
    {"BookID": "3", "Title": "Xinhua Zidian", "Author": "Wei Jiangong", "Available": "True"},
    {"BookID": "4", "Title": "Don Quixote", "Author": "Miguel de Cervantes", "Available": "True"},
    {"BookID": "5", "Title": "A Tale of Two Cities", "Author": "Charles Dickens", "Available": "True"},
    {"BookID": "6", "Title": "The Book of Mormon", "Author": "Joseph Smith", "Available": "True"},
]
# Initialize users list with data
org_users = [
    {"UserID": "1", "Name": "Alice Johnson", "Email": "alice.johnson@example.com"},
    {"UserID": "2", "Name": "Bob Smith", "Email": "bob.smith@example.com"},
    {"UserID": "3", "Name": "Charlie Brown", "Email": "charlie.brown@example.com"},
    {"UserID": "4", "Name": "Diana Prince", "Email": "diana.prince@example.com"},
    {"UserID": "5", "Name": "Eve Adams", "Email": "eve.adams@example.com"},
]
# Initialize transactions records (borrow/return)
org_transactions = [
    {"TransactionID": "1", "UserID": "U001", "BookID": "1", "Type": "Borrow", "Date": "2024-01-10"},
    {"TransactionID": "2", "UserID": "U002", "BookID": "2", "Type": "Borrow", "Date": "2024-01-12"},
    {"TransactionID": "3", "UserID": "U003", "BookID": "3", "Type": "Borrow", "Date": "2024-01-15"},
    {"TransactionID": "4", "UserID": "U004", "BookID": "4", "Type": "Return", "Date": "2024-01-20"},
    {"TransactionID": "5", "UserID": "U005", "BookID": "5", "Type": "Borrow", "Date": "2024-01-22"},
]