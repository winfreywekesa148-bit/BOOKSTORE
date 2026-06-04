#coffee class

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

        #size requires user input
        sizes = {
            "small": "small", 
            "medium": "medium", 
            "large": "large"
            }
        
        size_input = input("Please enter the coffee size (small, medium, large): ").lower()

        if size_input in sizes:
            print(f"You have selected a {size_input} coffee.")
        else:
            print(f"size must be small, medium, or large")

        #methods for tip
    def add_tip(self, tip_amount):
        tip_amount =+ 1.00

        if tip_amount > 0:
            print(f"total price: ${self.price + tip_amount:.2f}")
        else:
            print(f"total price: ${self.price:.2f}")


        