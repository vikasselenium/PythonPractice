

class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        print("calling getter method")
        return self._items

    @items.setter
    def items(self, items):
        print("calling setter method")
        if not isinstance(items, list):
            raise TypeError('items must be a list')
        self._items = items

my_backpack= Backpack()
print(my_backpack.items)

my_backpack.items = [123]
print(my_backpack.items)
