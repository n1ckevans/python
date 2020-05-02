class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        self.account_balance = User.account_balance
        return self

    def transfer_money(self, amount, User):
        self.account_balance -= amount
        User.account_balance += amount
        return self


nick = User("Nick Evans", "fake_email@gmail.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

nick.make_deposit(40).make_deposit(60).make_deposit(100).make_withdraw(20)
print("Nick has", nick.account_balance, "dollars in his account")

guido.make_deposit(1000).make_deposit(7000).make_withdraw(400).make_withdraw(1)
print("Guideo has", guido.account_balance, "dollars in his account")

monty.make_deposit(1000000).make_withdraw(500).make_withdraw(200).make_withdraw(500000)
print("Monty has", monty.account_balance, "dollars in his account")

monty.transfer_money(200000, nick)
print("Nick now has", nick.account_balance, "dollars in his account")