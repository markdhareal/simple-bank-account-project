class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        return f'Your Balance is: ${self.balance}'
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            self.check_balance()

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return f'Successful! You only have ${self.balance}'
        else:
            return 'Insufficient Funds'

    def __str__(self):
        return f'Owner: {self.name} Balance: {self.balance}'