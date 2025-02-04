class Bankaccaunt:
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Депозит: {amount}. Баланс: {self.balance} ")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Снятие: {amount}. Баланс: {self.balance}")
        else:
            print("Ошибка")


account = Bankaccaunt("Alibek", 1000)

account.deposit(400)

account.withdraw(300)
