# Simple Bank account System

```python
account_one = BankAccount('David', 2000)

print(account_one)
print(account_one.check_balance())
account_one.deposit(1000)
print(account_one)
print(account_one.withdraw(4000))
```

#### Sample Output:
> Owner: David Balance: 2000 <br>
> Your Balance is: $2000 <br>
> Owner: David Balance: 3000 <br>
> Insufficient Funds <br>
