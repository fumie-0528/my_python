class BankAccount:
	
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Balance is {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0: 
            int_rate = self.balance * self.int_rate
            print(int_rate)
        return self

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        self.account.deposit(100)

user_one = User("Michael", "micheal@yahoo.com")


