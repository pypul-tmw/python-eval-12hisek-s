class InsufficientBalanceError(Exception):
    pass

def withdraw(balance,amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough money")
    return balance - amount

try:
    print(withdraw(100,200))
except InsufficientBalanceError as e:
    print("Transaction failed!",e)