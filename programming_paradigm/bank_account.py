import os

class BankAccount:
    def __init__(self, initial_balance=0.0, storage_file="balance.txt"):
        self.storage_file = storage_file
        self.__account_balance = self._load_balance(initial_balance)  

    def _load_balance(self, default):
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    return float(file.read())
                except ValueError:
                    return default
        else:
            return default            

    def _save_balance(self):
        with open(self.storage_file, 'w') as file:
            file.write(str(self.__account_balance))

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance +=amount
            self._save_balance()
            
    def withdraw(self, amount):
        if 0 < amount <=self.__account_balance:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

       

