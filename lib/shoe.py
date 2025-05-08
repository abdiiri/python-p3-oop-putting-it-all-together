class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize _size
        self.size = size   # Use the setter to handle initial size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensuring size is an integer
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"