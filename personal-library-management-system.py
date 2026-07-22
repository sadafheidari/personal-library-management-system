
books= []
while True:


    print("="* 50)
    print ("PERSONAL LIBRARY MANAGEMENT SYSTEM")
    print("="* 50)
    print("\n1. Add a book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

    choice= input(" select your choice: ")

    if choice == '1':
        title = input("Enter the name of the book: ").strip()
        author = input("Enter the author: ").strip()
        year= input("Enter the year: ").strip()
        price = input("Enter the price: ").strip()
        book = {"title": title, "author": author, "year": year, "price": price,"status": "Available"}
        books.append(book)
        print(f"\ntitle of {title} added successfully")
        print()
    elif choice == "2" :

        print("======== َAvailable Books in the library =======")
        print()
        if len(books) == 0:
            print("No books available")
            print("=" *40)
            print()
        else:
            for book in books:
                print(f'\ntitle: {book["title"]} ,author: {book["author"]},year: {book["year"]},price: {book["price"]},status: {book["status"]}')
                print( "=" *40)
                print()

    elif choice == "3" :
        print("Searching for a book is selected")
        print()
    elif choice == "4":
        print("Removing a book is selected")
        print()
    elif choice == "5":
        print("Borrowing a book is selected")
        print()
    elif choice == "6":
        print("Returning a book is selected")
        print()
    elif choice == "7":
        print("Thank you for using Personal Library Management System!")
        print()
        break
    else:
        print("Please select a valid option")
        print()
