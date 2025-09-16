

class Circle:
    def __init__(self,radius):
        self.radius=radius

print("Before")
my_circle=Circle(5)
your_circle=my_circle

print(my_circle.radius)
print(your_circle.radius)

print("after")
your_circle.radius=12
print(my_circle.radius)
print(your_circle.radius)


class Backpack:

    backpack_cmpny='TATA'
    def __init__(self):
        self._items=[]

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self,new_list):
        self.items=self._items+new_list

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        self.items.remove(item)

    @classmethod
    def get_company_name(cls):
        return Backpack.backpack_cmpny

    @staticmethod
    def get_bag_info():
        print("This is a travelling bagpack with 40 ltr size")


my_backpack=Backpack()
my_backpack.add_item("water_bottle")
my_backpack.add_item("first aid kit")

print(my_backpack.items)

your_backpack=my_backpack
new_backpack=my_backpack

print(my_backpack is your_backpack is new_backpack)