#achieving method overloading in python
class Test1:
    def f1(self,*args):
        print("inside f1")
        x=1 #default value
        if len(args) == 0:
            print(x)
        elif len(args) == 2:
            print(sum(args))
        else:
            print(max(args))

t=Test1()
t.f1()
t.f1(12,22)
t.f1(12,2,222)

