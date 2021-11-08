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

account_one = BankAccount(int_rate = 0.35, balance = 500)
account_two = BankAccount(int_rate = 0.22, balance = 1000)

account_one.deposit(300).deposit(300).deposit(300).withdraw(200).yield_interest().display_account_info()
account_two.deposit(5000).deposit(3000).withdraw(400).withdraw(400).withdraw(400).withdraw(400).yield_interest().display_account_info()