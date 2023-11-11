from ex2.Account import Account
from ex2.CheckingAccount import CheckingAccounts
from ex2.SavingAccount import SavingAccount

def main():
    cont = Account(123456, 1000)
    print(cont)
    cont.withdraw(100)

    saving_cont=SavingAccount(123456, 1000, 0.1)
    print(saving_cont)
    saving_cont.withdraw(100)

    checking_cont=CheckingAccounts(123456, 1000, 1000)
    print(checking_cont)
    checking_cont.withdraw(100)
    print(checking_cont.get_balance())
    checking_cont.withdraw(2000)


if __name__ == '__main__':
    main()

