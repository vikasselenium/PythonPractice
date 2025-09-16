
import pack1.module1

#module1.f1() ==not working
pack1.module1.f1()

from pack1.module1 import f1
#highly recommended way
f1()

# it works even we delete __init__.py
# file is not mandatory in newer versions
