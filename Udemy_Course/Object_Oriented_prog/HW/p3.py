class Account:

    BALANCE = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account.BALANCE = self.balance
        print("Account owner:  "+self.owner) 
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        Account.BALANCE += amount
        print("Deposit Accepted")
        #return Account.BALANCE

    def withdraw(self, amount):
        if amount > Account.BALANCE:
            print("Funds Unavailable!")
        else:
            print("Funds Available")

acct1 = Account('Jose',100)
acct1.deposit(50)
acct1.withdraw(75)
    