class BankAccount:
    def __init__(self):
        self.bank_number = '12 3456 5555 9090 1111 0000 7722'
        self.bank_balance = 0
    
    def display_info(self):
        print(f"Bank Account No: {self.bank_number}")
        print(f"Balance: {self.bank_balance}")
        
    def deposit(self, deposit):
        self.bank_balance += deposit
        
    def withdraw(self, withdraw):
        if withdraw > self.bank_balance:
            print("Insufficient funds on the account")
        else:
            self.bank_balance -= withdraw