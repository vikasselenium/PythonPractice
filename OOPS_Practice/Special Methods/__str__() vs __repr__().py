from datetime import datetime

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __str__(self):
        return f"{self.name} on {self.date.strftime('%d-%b-%Y')}"  # Pretty for humans

    def __repr__(self):
        return f"Event(name='{self.name}', date=datetime({self.date.year}, {self.date.month}, {self.date.day}))"  # Reproducible
        #return f"{self.name} on {self.date.strftime('%d-%b-%Y')}"  # Pretty for humans
event = Event("Conference", datetime(2025, 8, 26))

print(str(event))   # Conference on 26-Aug-2025
print(repr(event))  # Event(name='Conference', date=datetime(2025, 8, 26))
