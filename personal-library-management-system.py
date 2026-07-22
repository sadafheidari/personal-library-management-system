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
    print("Adding a book is selected")
elif choice == "2" :
    print(" Viewing all books is selected")
elif choice == "3" :
    print("Searching for a book is selected")
elif choice == "4":
    print("Removing a book is selected")
elif choice == "5":
    print("Borrowing a book is selected")
elif choice == "6":
    print("Returning a book is selected")
elif choice == "7":
    print("Bye")
else:
    print("Please select a valid option")
