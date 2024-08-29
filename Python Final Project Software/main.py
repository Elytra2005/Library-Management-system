from Classes.book import Book
from Classes.library import Library

# Command Menue
def user_interface():
    print("Welcome to our library management system 3.0")
    print("Here are all of our menue items:")
    print("1. Add Book")
    print("2. Show all Books")
    print("3. Search for books")
    print("4. Check in a book")
    print("5. Check out a book")



def main():
    # creates library object
    LibrarySystem = Library()
    user_interface()
    while True:
        #main ask prompt
        askMain = int(input("Enter number: "))

        #adding books - Most important
        if askMain == 1:
            title = input("Enter title: ")
            ISBN = input("Enter Isbn: ")
            author = input("Enter author: ")
            # gives the book attributes value
            book_added = Book(ISBN, title, author)
            #adds book to add_book method
            LibrarySystem.add_book(book_added)
        elif askMain == 2:
            print("All Books - ")
            LibrarySystem.show_book()

        #searching for books
        elif askMain == 3:
            search = input("Enter book title: ")
            retrunBooks = LibrarySystem.find_book(search)
            if retrunBooks:
                print("Book found")
                for b in retrunBooks:
                    print(b)
            else:
                print("Book not found try again")
            
        #checking out
        elif askMain == 4:
            bookName = input("Enter book name: ")
            if LibrarySystem.return_book(bookName):
                pass

        #checking in
        elif askMain == 5:
            bookName = input("Enter book name: ")
            if LibrarySystem.put_in_book(bookName):
                pass
        else: 
            print("Invalid syntax try again: ")


if __name__ == "__main__":
    main()

    
