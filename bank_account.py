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
        if amount > self.balance:
            return f'you only have ${self.balance}'
        else:
            self.balance = self.balance - amount
            return f'Successful! You only have ${self.balance}'

    def __str__(self):
        return f'Owner: {self.name} Balance: {self.balance}'