# bank acc == owner, acc num, balance, history
from datetime import date, datetime
from time import strptime


class Client:
    def __init__(self, names:str, kra_pin:str, dob:str, gender:str):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)
        print(self.dob)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        age = today.year - birth_date.year
        return age

class BankAccount:
    def __init__(self, owner:Client, acc_no:str, balance:int):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)  # -100

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner)
        print(self.acc_no)
        print(self.balance)
        print(self.owner.names)
        print(self.owner.kra_pin)
        print("------------------------------")


Sofia = Client('Sofia Mohamed', 'A001', '2001-01-01', 'F')
Mohamed = Client('Mohamed Hassan', 'A002', '2006-01-01', 'M')

acc1 = BankAccount(Sofia, "11111", 70_000)
acc2 = BankAccount(Sofia, "22222", 80_567)
acc3 = BankAccount(Mohamed, "33333", 100_250_999)

acc1.deposit(10_000)
acc1.deposit(3000)

acc1.print_details()
acc1.withdraw(15_000)
acc1.print_details()

print("Sofia's Age", Sofia.calc_age())
print("Mohamed's Age", Mohamed.calc_age())

print(acc1.owner.calc_age())
print(acc2.owner.calc_age())





# dob = '26.07.2001'
#
# today = date.today()
# # print(f"{today.day}-{today.month}-{today.year}")
# #convert string to date
# birth_date = datetime.strptime(dob,  "%d.%m.%Y")
#
# age = today.year - birth_date.year
# print(age)

