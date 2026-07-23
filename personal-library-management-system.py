
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
        title = input("Enter the name of the book: ").strip().lower()
        author = input("Enter the author: ").strip().lower()
        year= input("Enter the year: ").strip()
        price = input("Enter the price: ").strip()
        book = {"title": title, "author": author, "year": year, "price": price,"status": "Available"}
        books.append(book)
        print(f"\ntitle of {title} added successfully")
        print()
    elif choice == "2" :

        print("======== Available Books in the library =======")
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
        search_title = input("Enter the book title to search: ").strip().lower()
        found = False
        for book in books:
            if book["title"] == search_title:
                print(f'\ntitle: {book["title"]} ,author: {book["author"]},year: {book["year"]},price: {book["price"]},status: {book["status"]}')
                found = True
                break
        if not found:
            print("The book title does not exist")
        print()
    elif choice == "4":
        remove_title = input("Enter the book title to remove: ").strip().lower()
        found = False
        for book in books:
            if book["title"] == remove_title:
                books.remove(book)
                print(f"the book title:{book['title']}removed successfully ")
                found = True
                break
        if not found:
            print("The book title does not exist")
        print()
    elif choice == "5":
        borrow_title = input("Enter the book title to borrow: ").strip().lower()
        found = False
        for book in books:
            if book["title"] == borrow_title:
                found = True

                if  borrow_title == "available":
                    book['status'] = 'Borrowed'
                    print(f"the book title:{book['title']} is borrowed ")
                else:
                    print(f"the book title:{book['title']} is already borrowed ")
                break
        if not found:
            print("The book title does not exist")
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
