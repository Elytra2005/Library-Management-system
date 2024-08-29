class Book:
    def __init__(self, ISBN, title, author, avalabilityStat = True):

        #Attributes that will be passed through args
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.avalabilityStat = avalabilityStat

    #returns all the data we will need
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Available: {self.avalabilityStat}"
    

    
