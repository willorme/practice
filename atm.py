from locale import currency
import locale
import time

locale.setlocale(locale.LC_ALL, '')

class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def get_balanace(self):
        return self.balance

    def get_name(self):
        return self.name



customers = [Customer('Amanda Keller', 22, 10000000.00),Customer('Will Orme', 23, 10000000.00)]
    


def withdraw():
    for customer in customers:

        q = input ('Enter amount to withdraw: ')
        new_balance = customer.balance - float(q)
        print('Withdrawing cash...')
        time.sleep(3)
        if float(q) > customer.balance:
            print ('Insufficient funds')
            continue
        else: 
            print('Your balance is now {}'.format(currency(float(new_balance))))
            break


def deposit():
    for customer in customers:
    
        q = input ('Enter amount to deposit: ')
        new_balance = customer.balance + float(q)
        print('Adding funds to your account...')
        time.sleep(3)
        if float(q) <= 0:
            print('Must deposit amount greater than 0')
            continue
        else:
            print('Your balance is now {}'.format(currency(float(new_balance))))
            break


def menu():
    print('################ Welcome to Orme Bank ##################')
   
    for customer in customers:

        main = input('Enter your name: ')
        if main == customer.name:
            print ('{}, your current balance is {}'.format(customer.name, currency(float(customer.balance))))
        else:
            print ('Name does not match existing account')
            continue
        wd = input('Would you like to withdraw or deposit? ')
        if wd == 'withdraw':
            withdraw()
            break
        elif wd == 'deposit':
            deposit()
            break
        else:
            print ('Invalid input')
        continue


menu()
            
        

        










