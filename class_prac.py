class BankAccount:
    # yahan initialize krna lazmi h !
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    # Yahan mene class k andar function banaya hai !
    # or iske andar mene amount pass kiya hai !
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")
    # Yahan bhi mene function banaya hai !
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")


# Create an object (instance)
account = BankAccount("Ali", 1000).deposit()

# Call methods on the object
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
