# direct execution
# indirect execution by importing module in another file
# __name__ => gives info about if direct or indirect execution
# __name__ => __main__  for direct execution

import module1

#print("test module1")
#print(__name__)
module1.add(300,2)