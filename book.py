#book class 
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
        #title requires user input
        if not self.title:
            raise ValueError("Title is required.")
        else:
            user_input = input("Please enter the book title: ")
            self.title = user_input
        
        #page_count requires user input
        if not self.page_count:
            raise ValueError("Page count is required.")
        else:
            user_input = input("Please enter the page count: ")
            self.page_count = int(user_input)

#method to turn pages
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
