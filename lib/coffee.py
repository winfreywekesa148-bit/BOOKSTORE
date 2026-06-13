#coffee class

class Coffee:
    VALID_SIZES = ["Small", "Medium", "Large"]

    def __init__(self, size, price):
        self._size = size
        self.price = price

    @property 
    def size(self):
        return self._size

    @size.setter
    def size(self, value):  
        if value in self.VALID_SIZES:
            self._size = value
        
        else:
            print(f"size must be Small, Medium, or Large")

        #methods for tip
    def tip(self, tip):
        tip =+ 1.00

        if tip > 0:
            print(f"total price: ${self.price + tip:.2f}")
        else:
            print(f"total price: ${self.price:.2f}")
            return tip


        