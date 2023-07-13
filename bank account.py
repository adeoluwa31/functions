class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into the account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from the account. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        print(f"Current balance: {self.balance}")



account1 = BankAccount("12345", "John Doe")
account2 = BankAccount("67890", "Jane Smith", 1000)


account1.deposit(500)
account1.get_balance()
account1.withdraw(200)
account1.get_balance()

account2.get_balance()
account2.withdraw(1500)
