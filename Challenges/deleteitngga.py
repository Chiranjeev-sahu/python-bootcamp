class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        print(f"Attempting to deposit: ${amount}")
        # Add validation
        if amount <= 0:
            print("Invalid deposit amount!")
            return False
        self.balance += amount
        print(f"New balance: ${self.balance}")
        return True

    def withdraw(self, amount):
        """
        Remove money from the account
        Intentional bug: Allows overdrawing
        """
        if amount > self.balance:
            print("Insufficient funds!")
            return False
        
        self.balance -= amount
        self.transactions.append(f"Withdrawal: -${amount}")
        return True

    def transfer(self, target_account, amount):
        print(f"Transfer attempt: ${amount}")
        print(f"Current balance: ${self.balance}")
        """
        Transfer money between accounts
        Intentional bug: No error handling
        """
        if self.withdraw(amount):
            target_account.deposit(amount)
            self.transactions.append(f"Transfer: -${amount} to {target_account.account_number}")
            return True
        return False

    def get_balance(self):
        """
        Check current balance
        """
        return self.balance

    def print_statement(self):
        """
        Print account statement
        Intentional bug: Might cause formatting issues
        """
        print(f"Account Statement for Account {self.account_number}")
        print("-" * 40)
        for transaction in self.transactions:
            print(transaction)
        print("-" * 40)
        print(f"Current Balance: ${self.balance}")

def main():
    """
    Demonstrate bank account operations with potential errors
    """
    try:
        # Create bank accounts
        checking = BankAccount("1234567", 1000)
        savings = BankAccount("7654321", 500)

        # Perform some transactions
        print("Initial Balances:")
        print(f"Checking: ${checking.get_balance()}")
        print(f"Savings: ${savings.get_balance()}")

        # Deposit money
        checking.deposit(500)
        
        # Intentional bug: Trying to deposit negative amount
        checking.deposit(-200)

        # Transfer between accounts
        checking.transfer(savings, 300)

        # Intentional bug: Try to overdraw
        checking.withdraw(2000)

        # Print statements
        print("\nChecking Account Statement:")
        checking.print_statement()

        print("\nSavings Account Statement:")
        savings.print_statement()

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()