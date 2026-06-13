#book class 
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        
        #title requires user input
        if not self.title:
            raise ValueError("Title is required.")
        else:
               self.title = title
        
        #page_count requires user input
        if not self.page_count:
            raise ValueError("Page count is required.")
        else:
            self.page_count = page_count

#method to turn pages
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
