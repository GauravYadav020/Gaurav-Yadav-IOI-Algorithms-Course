# Module 1 Lesson 5: After-Class Project
# Project Name: Cryptographically Secured ATM Terminal State Simulator

class SafeATMTerminal:
    def __init__(self, initial_vault_balance=50000, secure_pin="4932"):
        self.balance = initial_vault_balance
        self.pin = secure_pin
        self.authenticated = False

    def verify_credentials(self, input_pin):
        if input_pin == self.pin:
            self.authenticated = True
            return True
        return False

    def dispense_cash(self, requesting_amount):
        if not self.authenticated: return "Exception: Unauthorized Terminal Access."
        if requesting_amount > self.balance: return "Exception: Vault Reserve Insufficient."
        self.balance -= requesting_amount
        return f"Dispensation Success. Remaining Vault: ${self.balance}"

if __name__ == "__main__":
    atm = SafeATMTerminal()
    if atm.verify_credentials("4932"):
        print(atm.dispense_cash(12000))