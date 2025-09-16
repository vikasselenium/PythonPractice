class Employee:
    def __init__(self, name, base_salary, bonus_percent):
        self.name = name
        self.base_salary = base_salary
        self.bonus_percent = bonus_percent

    def calculate_bonus(self):
        """Calculates bonus based on percentage."""
        return self.base_salary * (self.bonus_percent / 100)

    def calculate_total_salary(self):
        """Returns total salary including bonus."""
        return self.base_salary + self.calculate_bonus()

    def display_details(self):
        """Displays employee details."""
        print(f"Employee Name: {self.name}")
        print(f"Base Salary: ₹{self.base_salary}")
        print(f"Bonus: ₹{self.calculate_bonus()}")
        print(f"Total Salary: ₹{self.calculate_total_salary()}")

emp1=Employee("Vikas",10000,10)
emp1.display_details()