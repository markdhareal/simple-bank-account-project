from bank_account import *

account_one = BankAccount('David', 2000)

print(account_one)
print(account_one.check_balance())
account_one.deposit(1000)
print(account_one)
print(account_one.withdraw(3000))
