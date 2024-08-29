from Classes.book import Book

class Library:
    #constructing the attr
    def __init__(self):
        #there will be the books stored
        self.booklist = []


    # Methods for library
    

    # Method to add a book
    def add_book(self, book_item):
        self.booklist.append(book_item)
        #displays that the book was added
        print(f"thank you we added '{book_item.title}' to our collection")

    # Method to display the books
    def show_book(self):
        if not self.booklist:
            print(f"{'book_item.title'} is not avalible please try again or check your spelling") #possibly display book title over here     
        else:
             for book_item in self.booklist:
                 print("we have found ", book_item)

    
    def find_book(self, Q):
        found = [] #all founded books searched will be stored here
        for book_item in self.booklist:
            found.append(book_item)
            return found
        
    def return_book(self, returnTitle):
        for book_item in self.booklist:
            if book_item.avalabilityStat:
                # Makes the avalability status of the book false
                book_item.avalabilityStat = False
                print("Your Book has sucessfully been checked out!")
                return
            else:
                print(f"{book_item.title} does not exist")

    def put_in_book(self, bringTitle):
        for book_item in self.booklist:
            book_item.avalabilityStat = True
            print(f"checked in {book_item.title}")
            return True
        return False
                

            








    

       

    

