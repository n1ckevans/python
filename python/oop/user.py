class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        self.account_balance = User.account_balance

    def transfer_money(self, amount, User):
        self.account_balance -= amount
        User.account_balance += amount


nick = User("Nick Evans", "fake_email@gmail.com")
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

nick.make_deposit(40)
nick.make_deposit(60)
nick.make_deposit(100)
nick.make_withdraw(20)
print("Nick has", nick.account_balance, "dollars in his account")

guido.make_deposit(1000)
guido.make_deposit(7000)
guido.make_withdraw(400)
guido.make_withdraw(1)
print("Guideo has", guido.account_balance, "dollars in his account")

monty.make_deposit(1000000)
monty.make_withdraw(500)
monty.make_withdraw(200)
monty.make_withdraw(500000)
print("Monty has", monty.account_balance, "dollars in his account")

monty.transfer_money(200000, nick)
print("Nick now has", nick.account_balance, "dollars in his account")