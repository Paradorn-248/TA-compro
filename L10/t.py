import json


class Account:
    def __init__(self, name, account_number, money, history):
        self.name = name
        self.account_number = account_number
        self.money = money
        self.history = history

    def show_data(self):
        print(f'Name : {self.name}')
        print(f'Account number : {self.account_number}')
        print(f'Money : {self.money}')
        print(f'History : {self.history}')

    def deposit(self):
        amount = int(input('Amount : '))
        self.money += amount
        if self.history == '':
            self.history = f'Deposit : {amount}'
        else:
            self.history += f'\nDeposit : {amount}'
        print(f'Current money : {self.money}')

    def withdraw(self):
        amount = int(input('amount : '))
        self.money -= amount
        if self.history == '':
            self.history = f'Withdraw : {amount}'
        else:
            self.history += f'\nWithdraw : {amount}'
        print(f'Current money : {self.money}')

    def show_history(self):
        print(self.history)

filename = input('Filename : ')
with open(filename) as f:
    data = json.load(f)

classes = []
for account in data:
    classes.append(Account(
        account['name'], account['account number'], account['money'], account['history']))

while True:
    acc_num = input('Account number : ')
    for account in classes:
        if account.account_number == acc_num:
            while True:
                menu = input('Menu : ')
                if menu == '0':
                    break
                elif menu == '1':
                    account.show_data()
                elif menu == '2':
                    account.deposit()
                elif menu == '3':
                    account.withdraw()
                elif menu == '4':
                    account.show_history()
                elif menu == '5':
                    continue
    break

check = input()
if check == '01':
    classes[0].show_data()
elif check =='02' :
    classes[0].deposit()
elif check =='03' :
    classes[0].withdraw()
elif check =='04' :
    classes[0].show_history()
