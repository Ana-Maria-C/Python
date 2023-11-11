from ex2.Account import Account


class SavingAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate

    def __str__(self):
        return f'SavingAccount with balance: {str(self.balance)} and interest rate: {str(self.interest_rate)} has interest: {str(self.calculate_interest())}'