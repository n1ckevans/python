class BankAccount:
    def __init__(self, interest=0, balance = 0):
        self.balance = balance
        self.interest = interest * 0.01

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.interest > 0:
            print("Yield interest is", self.balance * self.interest)
            return self

account1 = BankAccount(1, 10000)
account2 = BankAccount(5)

account1.deposit(300).deposit(1000).deposit(50).withdraw(500).yield_interest().display_account_info()
account2.deposit(50000).deposit(10).withdraw(5).withdraw(10).withdraw(20).withdraw(1000).yield_interest().display_account_info()