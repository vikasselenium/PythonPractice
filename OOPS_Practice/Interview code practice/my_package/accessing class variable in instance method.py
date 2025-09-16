
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show(cls):
        print("Count:", Counter.count)

c1 = Counter()
c1.show()
