borrowed_books = []

def borrow_book():
    name = input("Enter borrower name: ")
    book = input("Enter book title: ")
    borrowed_books.append({"name": name, "book": book})
    print("Book borrowed successfully")

def view_borrowed_books():
    if not borrowed_books:
        print("No borrowed books found")
    else:
        for record in borrowed_books:
            print(record["name"], "- Borrowed:", record["book"])

def main():
    while True:
        print("1. Borrow Book")
        print("2. View Borrowed Books")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            borrow_book()
        elif choice == "2":
            view_borrowed_books()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
