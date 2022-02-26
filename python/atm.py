from locale import currency
import locale
import time

locale.setlocale(locale.LC_ALL, '')

class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

customers = [Customer('Jeff Johnson', 22, 10000000.00), 
             Customer('Will Orme', 23, 20000000.00), 
             Customer('Jack Black', 26, 25.00),
             Customer('Amanda Keller', 22, 1000000.00),
             Customer('Steve Orme', 22, 10.00),
             Customer('Jeff Bezos', 50, 248000000000.00)
             ]


print('################ Welcome to Orme Bank ##################')
main = input('Enter your name: ')  

def transaction():
   
    for customer in customers:

        
        balance = customer.balance
        name = customer.name

        if main != name:
            continue
        else:
            print ('{}, your current balance is {}'.format(name, currency(float(balance))))

        while customer.name:
            wd = input('Would you like to withdraw or deposit? ')
            if wd == 'withdraw':
                q = input ('Enter amount to withdraw: ')
                new_balance = balance - float(q)
                if float(q) > balance:
                    print ('Insufficient funds')
                else:
                    print('Withdrawing cash...')
                    time.sleep(3)
                    print('Your balance is now {}'.format(currency(float(new_balance))))
                    break
                
            elif wd == 'deposit':
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
        break



transaction()
        










