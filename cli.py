import json

from main import add_deposit, check_balance, add_withdrawal, list_transactions, save_ledger, load_ledger, InvalidAmountError, InsufficientFundsError

load_ledger()




while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Account Balance")
    print("4. View All Transactions")
    print("5. Exit")
    choice = int(input("Select Option To Proceed:"))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        break




