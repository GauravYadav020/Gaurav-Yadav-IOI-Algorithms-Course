# Module 6 Lesson 2: After-Class Project
# Project Name: Multi-Tier Retail Banking Inheritance & Polymorphism Ledger

class BaseBankCustomerAccount:
    def __init__(self, account_number, holder_name, initial_balance=0.0):
        self.acc_num = account_number
        self.name = holder_name
        self.balance = initial_balance

    def post_deposit(self, cash_amount):
        if cash_amount > 0: self.balance += cash_amount

    def post_withdrawal(self, cash_amount):
        if 0 < cash_amount <= self.balance:
            self.balance -= cash_amount
            return True
        return False

class PremiumCorporateAccount(BaseBankCustomerAccount):
    def __init__(self, account_number, holder_name, initial_balance=0.0, overdraft_limit=50000.0):
        super().__init__(account_number, holder_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def post_withdrawal(self, cash_amount):
        # Polymorphic behavior overriding standard balance checks with overdraft facilities
        if 0 < cash_amount <= (self.balance + self.overdraft_limit):
            self.balance -= cash_amount
            return True
        return False

if __name__ == "__main__":
    corp_acc = PremiumCorporateAccount("ACC-CORP-99", "Tech Giants Inc.", 10000, 20000)
    print(f"Overdraft withdrawal status: {corp_acc.post_withdrawal(25000)} | New Balance context: ${corp_acc.balance}")