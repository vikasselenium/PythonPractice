
# for indexing the Object
# obj[index] -> __getitem__()

# my_list=[13,4,5,56,6,63,3]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print("##################")
# print(my_list.__getitem__(0))
# print(my_list.__getitem__(1))
# print(my_list.__getitem__(2))

class Bookshelf:
    def __init__(self):
        self.content=[[],
                      [],
                      []]

    def add_book(self,book,location):
        self.content[location].append(book)

    def take_book(self,book,location):
        self.content[location].remove(book)

    def __getitem__(self,location):
        return self.content[location]

my_book_shelf=Bookshelf()
my_book_shelf.add_book("ABC",0)
my_book_shelf.add_book("XYZ",0)
my_book_shelf.add_book("LMN",0)

my_book_shelf.add_book("__ABC",1)
my_book_shelf.add_book("__XYZ",1)
my_book_shelf.add_book("__LMN",1)

print(my_book_shelf[0])
print(my_book_shelf[1])