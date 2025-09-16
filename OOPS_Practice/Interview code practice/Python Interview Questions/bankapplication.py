
class BankLoan:
    bank_name="HSBC"

    def __init__(self, account_id, age, principal):
        self._principal=principal
        self._account_id=account_id
        self._age=age
        self.roi=0
        if self._age <= 0 or self._age >= 100:
            #print("please enter valid age")
            raise ValueError("Age must be between 1 and 199")
        else:
            if self._age >= 60:
                self.roi=6
            elif self._age < 60:
                self.roi=8

    def get_amount(self):
        return self._principal

    def get_age(self):
        return self._age

    def calculate_loan(self):
         return  (self._principal*1*self.roi)/100


b1=BankLoan("ABC123", 650, 10000)
print(b1.calculate_loan())