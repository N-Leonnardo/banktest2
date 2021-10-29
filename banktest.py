class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 100

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        (other_user).account_balance += amount
        print (str(amount))
        
guido = User("Guidim Silva", "mcleocrel@gmail.com")

guida = User("Guidinha Silva", "meucanalleo@gmail.com")

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()