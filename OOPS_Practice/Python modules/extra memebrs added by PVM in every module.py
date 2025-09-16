'''

This modules contains some of builtin members of module


'''
#  to hold doc string => __doc__
#  to hold file name => __file__
#  __name__ =>
#  which loader responsible for loading module => __loader__
#  this module related to which package = __package__
# __spec__
# __bulletin__

# programmer can also use these members  based on requirement

import module1
import os

x=888
y=999

def add(x,y):
    return x+y
print(dir(),end='')
# print(__doc__)
print("file used: ", __file__)
print("file absolute path: ", os.path.abspath(__file__))
print("file present in dir : ", os.path.dirname(__file__))
print("Package name: ", __package__)
print("__builtins__ name: ", __builtins__)
print("__loader__ name: ", __loader__)

print("file used: ", module1.__file__)



