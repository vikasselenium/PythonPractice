
# my_string="Hello World!"
# print(len(my_string))
# print(my_string.__len__())

# my_list=[1,4,3,5,6,7]
# print(len(my_list))
# print(my_list.__len__())

# my_tuple=(1,3,44,55,66,7,7)
# print(len(my_tuple))
# print(my_tuple.__len__())

# my_dict={1:"one", 2:"two", 3:"three"}
# print(len(my_dict))
# print(my_dict.__len__())

# we override this method for getting object len
class Backpack:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item is not present in the Backpack")

    def __len__(self):
        return len(self.items)

backpack=Backpack()
print(len(backpack))
backpack.add_item("water bottle")
backpack.add_item("sleeping bag")
backpack.add_item("Laptop charger")

print(len(backpack))
backpack.remove_item("sleeping bag")
print(len(backpack))