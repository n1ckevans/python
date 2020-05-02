class User:
    def __init__(self, username, account_id, email):
        self.name = username
        self.email = email
        self.account_id = account_id
        self.account = BankAccount(interest=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit()

    def make_withdraw(self, amount):
        self.account.withdraw()

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, amount, User):
        self.account.balance -= amount
        User.account.balance += amount

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