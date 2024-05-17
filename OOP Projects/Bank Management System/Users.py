from abc import ABC, abstractmethod
from datetime import datetime
from Bank import Bank
class Account:
    def __init__(self, name, email, address, account_type, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.password = password
        self.balance = 0
        self.account_id = 0
class User(Account):
    def __init__(self, name, email, address, account_type, password) -> None:
        super().__init__(name, email, address, account_type, password)
        self.transection_history = []
        self.loans = 0
        self.lone_time = 0
        self.account_id = 100 + len(Bank.users)
        Bank.users.append(self)

    def deposit(self, bank, amount):
        if amount > 0:
            self.balance += amount
            bank.balance += amount  
            self.transection_history.append(f"{datetime.now()} Deposit {amount}")

    def withdrow(self, bank, amount):
        if self.balance >= amount and amount > 0:
            if bank.bank_status == True:
                print("The Bank Is Bankrupt") 
                return
            self.balance -= amount
            bank.balance = amount
            self.transection_history.append(f"{datetime.now()} Withdrow {amount}")
        else:
            print("Withdrow Amount Exceeded")

    def check_balance(self):
        print(f"{self.name} Your Account Balance Is {self.balance} Now!!!")

    def check_history(self):
        print("----------\n")
        print("-----History-----")
        print(f"-----Date\t\tAmount-----")
        for history in self.transection_history:
            print(history)
        print("\n--------------------\n")

    def take_loan(self, bank, amount):
        if self.loan_time < 2 and bank.balance >= amount and bank.bank_status == False and amount > 0 and bank.loan_status == True:
            self.loan_time += 1
            bank.balance -= amount
            self.loans += amount
            print(f"You Took Loan Successfully {amount} TK!!!")
        else:
            print("Sorry Your Request Is Rejected???")

    def transfar_money(self, bank, account_id, amount):
        if self.balance >= amount:
            account = bank.find_account(account_id)
            if account:
                self.balance -= amount
                account.balance += amount
                print(f"{amount} TK Successfully Transfer {account_id}")
            else:
                print("Account Does Not Exist!!!")
        else:
            print("Sorry Your Request Is Cancelled!!!")

    def show_balance(self):
        print(f"{self.account_id} Your Current Balance Is {self.balance}")                

class Admin(Account):
    def __init__(self, name, email, address, account_type, password) -> None:
        super().__init__(name, email, address, account_type, password)
        Bank.admin.append(self)

    def add_money_to_bank(self, bank, money):
        if money > 0:
            bank.add_money(money)

    def show_bank_balance(sekf, bank):
        bank.show_balance()

    def see_all_user_account_list(self, bank):
        bank.show_all_users()

    def delete_user(self, bank, id):
        bank.delete_user(id)

    def set_loan_status(self, bank, status):
        bank.loan_status(status)

    def show_total_loans_amount(self, bank):
        t = bank.total_loans_amount()
        print(f"The Total Loans Taken By User Are : {t} TK!!!")            
