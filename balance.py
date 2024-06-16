from globals import *

class Balance: #observable singleton
    def __new__(cls) -> None:
        if not(hasattr(cls, "instance")):
            cls.instance = super(Balance, cls).__new__(cls)
        return cls.instance
        
    def __init__(self):
        self.__stored_amount = 0

    def get_amount(self):
        amount = self.__stored_amount
        return amount

 
    def set_deposit(self):
        while True:
            deposit = input("enter your deposit $")

            if deposit.isdigit():
                deposit = int(deposit)
                if 0 < deposit < MAX_DEPOSIT:
                    break
                else:
                    print("Deposit must be greater than 0")
                    continue
            else:
                print("Deposit must be a whole positive amount")
                continue
        self.__add_to_balance(deposit)
        return True
    
    def __add_to_balance(self, amount):
        self.__stored_amount += amount


if __name__ == "__main__":
    balance = Balance()
    print(f"{balance.get_amount() = }")
    balance.set_deposit()
    print(f"{balance.get_amount() = }")