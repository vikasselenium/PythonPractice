

import inspect

def getinfo():
    print("caller Module", inspect.stack()[1][1])
    print("caller function name",inspect.stack()[1][3])

