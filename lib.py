
# database 
books=[]
issued_books=[]
def add_book():
    name=input("Enter the Book Name:")
    books.append(name)
    print(name ,"is added")
def show_books():
    if len(books)==0:
        print("No books Available")
    else:
        print("Available Books")
        for book in books:
            print(book)
    print("_________________________________________________________________________________")
def issue_book():
    available=input("Enter the book name:")
    if available in books:
        books.remove(available)
        issued_books.append(available)
        print(available, "book issued")
    else:
        print(available, "not available")
def return_book():
    Return=input("Enter the book name:")
    if Return in issued_books:
        issued_books.remove(Return)
        books.append(Return)
        print(Return, "Book Retuened")
    else:
        print(Return, ", This book was not issued")
    



    
        
    
    
    
def library():
    while True:
        print("\nMenu")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Show Books")
        print("4. Return Book")
        print("5. Exit")
        choice=int(input("\n Enter Your Choice:"))
        if choice==1:
            add_book()
        elif choice==2:
            issue_book()
        elif choice==3:
            show_books()
        elif choice==4:
            return_book
        elif choice==5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")
library()