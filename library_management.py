# Library Book Management System
library = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter published year: ")

    library.append({
        "title": title,
        "author": author,
        "year": year
    })

    print("Book added successfully!\n")

def view_books():
    if len(library) == 0:
        print("No books available.\n")
        return
    
    print("\n--- List of Books ---")
    for b in library:
        print(f"Title: {b['title']} | Author: {b['author']} | Year: {b['year']}")
    print()
def search_book():
    keyword = input("Enter keyword to search: ").lower()

    found = False
    print("\n--- Search Results ---")
    for b in library:
        if keyword in b["title"].lower() or keyword in b["author"].lower():
            print(f"Title: {b['title']} | Author: {b['author']} | Year: {b['year']}")
            found = True

    if not found:
        print("No matching books found.")
    print()
def menu():
    while True:
        print("===== Library Book Management =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again!\n")

menu()