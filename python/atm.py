from calendar import c
from locale import currency
import locale
import time

locale.setlocale(locale.LC_ALL, '')

class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    
    def __repr__(self) -> str:
        return self.name, self.age, self.balance

customers = [Customer('Jeff Johnson', 22, 10000000.00), 
             Customer('Will Orme', 23, 20000000.00), 
             Customer('Jack Black', 26, 25.00),
             Customer('Amanda Keller', 22, 1000000.00),
             Customer('Steve Orme', 22, 10.00),
             Customer('Jeff Bezos', 50, 248000000000.00),
             Customer('Kathryn Orme', 19, 50000.00)]


def add_customers(customer_list):

    customers.extend(customer_list)

    return customer_list


print('################ Welcome to Orme Bank ##################')

def transaction():
    
    main = input('Enter your name: ')
    
    for customer in customers:

        balance = customer.balance
        name = customer.name
    
        
        if main != name:
            continue
        else:
            print ('{}, your current balance is {}'.format(name, currency(float(balance))))
   


        while customer.name:
            wd = input('If you would like to withdraw, enter "w". If you would like to deposit, enter "d". ')
            if wd == 'w':
                q = input ('Enter amount to withdraw: ')
                new_balance = balance - float(q)
                if float(q) > balance:
                    print ('Insufficient funds')
                else:
                    print('Withdrawing cash...')
                    time.sleep(3)
                    print('Your balance is now {}'.format(currency(float(new_balance))))
                    break
                
            elif wd == 'd':
                q = input ('Enter amount to deposit: ')
                new_balance = balance + float(q)
                if float(q) <= 0:
                    print('Must deposit amount greater than 0')
                else:
                    print('Adding funds to your account...')
                    time.sleep(3)
                    print('Your balance is now {}'.format(currency(float(new_balance))))
                    break
                

            else:
                print ('Invalid input')
                continue
        

add_customers([Customer('James Brown', 67, 5.00), Customer('Tom Brady', 23, 400000000.00), Customer('Kirk Cousins', 32, 84000000.00)])

transaction()
        










