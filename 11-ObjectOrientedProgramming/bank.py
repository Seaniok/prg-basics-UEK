from bankaccount import BankAccount

def main():
    
    account = BankAccount()
    
    account.deposit(25.30)
    account.display_info()
    account.withdraw(31.70)
    account.display_info()
    account.withdraw(14)
    account.display_info()
    
if __name__ == '__main__':
    main()