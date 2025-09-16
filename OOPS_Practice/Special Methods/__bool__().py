
# bank account
class BankAccount:
    def __init__(self,account_name, account_id, balance):
        self.account_name=account_name
        self.account_id=account_id
        self.balance=balance

    def make_deposite(self,amount):
        self.balance=self.balance+amount

    def make_withdrawal(self,amount):
        if self.balance - amount >=0:
            self.balance= self.balance-amount
        else:
            print("Insufficient balance")

    def __bool__(self):
        if self.balance <= 0:
            return False
        else:
            return True

    def __str__(self):
        return f"Account details: {self.account_name},{self.account_id}, {self.balance}"

my_bank=BankAccount("Vikas","23232-3434-34344",3000)
print(my_bank)
my_bank.make_deposite(4000)
print(my_bank)
print(bool(my_bank))
my_bank.make_withdrawal(7000)
print(my_bank)
print(bool(my_bank))