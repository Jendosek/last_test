#11
class BankAccount:
    def __init__(self,  account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        self.balance += 200
    def withdraw(self):
        self.balance -= 100

get_info = BankAccount(account_number = "nsdh3nfs521gmd3", balance = 1000)
print(f"Ім'я банка: {get_info.account_number}")
print(f"Початковий баланс: {get_info.balance}")

get_info.deposit()
get_info.withdraw()

print(f"Кінцевий баланс: {get_info.balance}")

