class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        self.__balance = initial_balance if initial_balance >= 0 else 0.0

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
