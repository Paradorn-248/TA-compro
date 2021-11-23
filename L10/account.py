# สร้างบัญชีเก็บเงินของคนแล้วมีฟังก์ชันบอกข้อมูล ฝากเงิน ถอนเงิน โดยอ่านจากไฟล์jsonที่ให้มา แล้วเก็บเป็นลิสของclassไว้
import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

class Account :
    def __init__(self,name,acc_num,money,history):
        self.name = name
        self.acc_num = acc_num
        self.money = money
        self.history = history
        
    def show_data(self) :
        print(f"Name : {self.name}\nAccount number : {self.acc_num}\nMoney : {self.money}\nHistory : {self.history}")
    
    def deposit(self) :
        m = int(input("Amount : "))
        self.money += m
        print("Current money :",self.money)
        if self.history == '' :
            self.history += f'Deposit : {m}'
        else :
            self.history += f'\nDeposit : {m}'

    def withdraw(self) :
        m = int(input("amount : "))
        self.money -= m
        print("Current money :",self.money)
        if self.history == '' :
            self.history += f'Withdraw : {m}'
        else :
            self.history += f'\nWithdraw : {m}'

    def show_history(self) :
        print(self.history)

def acc_index(classes) :
    acc_number = input("Account number : ")
    for i in range(len(classes)) :
        if classes[i].acc_num == acc_number :
            return i

filename = input("Filename : ")
datas = read_json(filename)
classes = list()
for i in range(len(datas)) :
    data = Account(datas[i]['name'],datas[i]['account number'],datas[i]['money'],datas[i]['history'])
    classes.append(data)
index = acc_index(classes)
while(True) :
    menu = int(input("Menu : "))
    if menu == 0 :
        break
    elif menu == 5:
        index = acc_index(classes)
    elif menu == 1 : # show data
        classes[index].show_data()
    elif menu == 2 : # deposit
        classes[index].deposit()
    elif menu == 3 : # withdraw
        classes[index].withdraw()
    elif menu == 4: # show history
        classes[index].show_history()

# check function
check = input()
if check == '01':
    classes[0].show_data()
elif check =='02' :
    classes[0].deposit()
elif check =='03' :
    classes[0].withdraw()
elif check =='04' :
    classes[0].show_history()