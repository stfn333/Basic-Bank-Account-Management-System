class BankAccount:
    """
        Represents a basic bank account.

        Attributes:
        __account_number (str): The account number.
        __balance (float): The current balance in the account.
        """

    def __init__(self, account_number, balance=0.00):
        """
        Constructor method to initialize the account number and balance.

        Parameters:
        account_number (str): The account number.
        balance (float): The initial balance (default is 0.00).
        """
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.

        Parameters:
        amount (float): The amount to deposit.
        """
        self.__balance += amount
        print(f"Deposited ${amount:.2f}.\nNew balance: ${self.__balance:.2f}")

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount:.2f}.\nNew balance: ${self.__balance:.2f}")
        else:
            print("Insufficient funds.\nWithdrawal canceled.")

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        print(f"Your current balance is ${self.__balance:.2f}")

    def return_balance(self):
        """
        Returns the current balance.

        Returns:
        float: The current balance.
        """
        return self.__balance


class SavingsAccount(BankAccount):
    """
    Represents a savings account, inheriting from BankAccount.

    Attributes:
    __interest_rate (float): The interest rate for the savings account.
    """
    def __init__(self, account_number, balance=0.00, interest_rate=0.00):
        """
        Represents a savings account, inheriting from BankAccount.

        Attributes:
        __interest_rate (float): The interest rate for the savings account.
        """
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        current_balance = super().return_balance()
        interest_earned = current_balance * (self.__interest_rate / 100)
        new_balance = current_balance + interest_earned
        print(f"Interest earned: ${interest_earned:.2f}.\nNew balance: ${new_balance:.2f}")


def main():
    """
    Main function to run the basic account management system.
    """
    print("=======Welcome=======")
    account_number = input("Enter your account number: ")
    balance = input("Enter your balance: ")

    if not balance.isnumeric() or float(balance) < 0:
        print("Please, enter a valid balance!")
    else:
        balance = float(balance)
        bank_account = BankAccount(account_number, balance)
        while True:
            print("""
            =======Options=======
            [1] Check balance
            [2] Make a deposit
            [3] Withdraw
            [4] Open a Savings Account
            [5] Exit
            """)
            choice = input("Choose an option: ")

            if not choice.isnumeric():
                print("Please enter a valid choice.")
                continue
            else:
                choice = int(choice)
                if choice < 1 or choice > 5:
                    print("Please enter a valid choice. ")
                    continue
                else:
                    if choice == 5:
                        print("Goodbye.")
                        break
                    elif choice == 1:
                        bank_account.get_balance()
                    elif choice == 2:
                        deposit = input("Enter your deposit: ")
                        if not deposit.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            deposit = float(deposit)
                            if deposit < 0:
                                print("Enter a valid amount.")
                            else:
                                bank_account.deposit(deposit)
                    elif choice == 3:
                        withdraw = input("Enter amount: ")
                        if not withdraw.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            withdraw = float(withdraw)
                            if withdraw < 0:
                                print("Enter a valid amount.")
                            else:
                                bank_account.withdraw(withdraw)
                    elif choice == 4:
                        interest_rate = input("Enter the interest rate: ")
                        if not interest_rate.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            interest_rate = float(interest_rate)
                            if interest_rate < 0:
                                print("Enter a valid amount.")
                            else:
                                account_balance = bank_account.return_balance()
                                savings_account = SavingsAccount(account_number, account_balance, interest_rate)
                                savings_account.calculate_interest()


# Initialize the program.
if __name__ == "__main__":
    main()
