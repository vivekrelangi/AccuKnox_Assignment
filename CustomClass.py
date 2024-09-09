"""Below is the custom class created for the given requirements in the assignment"""
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(10, 5)
for dim in rect:
    print(dim)

# Output:
# {'length': 10}
# {'width': 5}
