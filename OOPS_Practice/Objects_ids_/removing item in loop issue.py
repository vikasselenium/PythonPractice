
def remove_item_from_dict(dict):
    for key,value in dict.items():
        if value%2==0:
            del dict[key]

my_dict={"1":1,"2":2,"3":3,"4":4}
remove_item_from_dict(my_dict)

