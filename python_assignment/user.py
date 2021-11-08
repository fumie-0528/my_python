class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount
        return self
    
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"Balance is {self.amount}")
        return self

    def transfer_money(self, to_user, amount):
        self.make_withdrawal(amount)
        to_user.make_deposit(amount)

user_one = User("Michael")
print(user_one.name)
user_one.make_deposit(300).make_deposit(500).make_deposit(1000).make_withdrawal(400).display_user_balance()
user_two = User("Chad")
print(user_two.name)
user_two.make_deposit(5000).make_deposit(8000).make_withdrawal(200).make_withdrawal(10000).display_user_balance()
user_three = User("Karen")
print(user_three.name)
user_three.make_deposit(600000).make_withdrawal(1000).make_withdrawal(1000).make_withdrawal(1000).display_user_balance()

user_one.transfer_money(user_two, 200)
user_one.display_user_balance()
