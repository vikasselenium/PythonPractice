
class Backpack:

    # class Variable
    backpack_id = 1 # class Variable, for tracking id_creation

    #constructor
    def __init__(self):
        self._items = []
        self.id= Backpack.backpack_id
        Backpack.backpack_id = Backpack.backpack_id +1

    #constructor overloading is not supported in python
    # def __init__(self, color):
    #     self._items = []
    #     self.color= color
    #     self.id= Backpack.backpack_id
    #     Backpack.backpack_id = Backpack.backpack_id +1

    # def __init__(self, color="red"):
    #     self._items = []
    #     self.color = color
    #     self.id = Backpack.backpack_id
    #     Backpack.backpack_id = Backpack.backpack_id + 1

    #constructor overloading using *args

    def __init__(self, *args):
        # default values
        self._items = []
        self.color = "red"

        if len(args) == 1:
           if isinstance(args[0],str):
               self.color = args[0]
        elif len(args) == 2:
            if isinstance(args[0],str) and isinstance(args[1],list):
                self.color = args[0]
                self._items = args[1]

        self.id = Backpack.backpack_id
        Backpack.backpack_id += 1

    #Read-only getter method
    @property
    def items(self):
        return self._items

    # setter method
    @items.setter
    def items(self,new_list):
        if isinstance(new_list, list):
            self._items.extend(new_list)
        else:
            print("Add valid list")


    #instance methods
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Enter valid value")
        return self #this is used for method chaining

    def remove_item(self,item):
        if item in self._items:
            self._items.remove(item)
        else:
            print("Backpack doesnt contain this item")

    def has_item(self,item):
        if item in self._items:
            return True
        else:
            return False

    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item) # here we are using self to call another method


print("+++++my backpack+++++")
my_backpack=Backpack()
print(my_backpack.id)
print(my_backpack.color)

print("+++++your backpack+++++")
your_backpack=Backpack("Green")
print(your_backpack.id)
print(your_backpack.color)

#passing list as an argument
print("+++++new backpack+++++")
new_backpack = Backpack("yellow",["umbrella","water bottle"])
print(new_backpack.id)
print(new_backpack.color)
print(new_backpack.items)

print("+++++++++Method chaining example++++++++++")
new_backpack.add_item("orange").add_item("A").add_item("B").add_item("C").add_item("D")
print(new_backpack.id)
print(new_backpack.items)



# print("+++++new backpack+++++")
# new_backpack=Backpack()
# print(new_backpack.id)

# print(my_backpack.items)
# my_backpack.add_item("Umbrella")
# my_backpack.add_item("First Aid kit")
# my_backpack.add_item("Water Bottle")
# print(my_backpack.items)
# my_backpack.remove_item("Umbrella")
# print(my_backpack.items)
#
# print(my_backpack.has_item("Umbrella"))
# print(my_backpack.has_item("Water Bottle"))
#
# my_backpack.items=['A','B','C']
# print(my_backpack.items)