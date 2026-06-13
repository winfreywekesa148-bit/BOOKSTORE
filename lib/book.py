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
        
    def page_count(self, page):
         if isinstance(page, int):
              self.page_count = page
         else:
              print("page_count must be in integer")

#method to turn pages
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
