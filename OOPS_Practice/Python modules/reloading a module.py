
import time
import module1
#from imp import reload #depricated from python 3.4 onwards

from importlib import reload



module1.add(10,20)
time.sleep(40)

#import module1
#module1.product(10,20) #AttributeError: module 'module1' has no attribute 'product' -if now re-load
#module1.product(10,20) #AttributeError: module 'module1' has no attribute 'product' -if now re-load

reload(module1)
module1.product(10,20)