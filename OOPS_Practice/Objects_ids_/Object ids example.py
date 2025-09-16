
class Backpack:
    def __init__(self):
        print("Calling constructor")
        self._items=[]

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self,new_items):
        if isinstance(new_items,list):
            self._items=new_items

B1=Backpack()
B1.items.append("orange")
print(B1.items)

B2=Backpack()
B2.items.append("Green")
print(B2.items)

print("++++++++++ids++++++++++++++++++")
print(id(B1))
print(id(B2))
print("++++++++++ids++++++++++++++++++")

