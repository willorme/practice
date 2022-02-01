from locale import currency
import locale

locale.setlocale(locale.LC_ALL, '')

class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance




customers = [Customer('Amanda Keller', 22, 10000000),Customer('Will Orme', 23, 10000000)]

def withdraw():
    for customer in customers:
        q1 = input ('Enter your name: ')
        if q1 == customer.name:
            print ('{}, your current balance is {}'.format(customer.name, currency(int(customer.balance))))
        else:
            print ('Name does not match any account')
            break
        q2 = input ('Enter amount to withdraw: ')
        new_balance = customer.balance - int(q2)
        if int(q2) > customer.balance:
            print ('Insufficient funds')
            break
        else: 
            print('Your balance is now {}'.format(currency(int(new_balance))))
            break

def deposit():
    for customer in customers:
        q1 = input('Enter your name: ')
        if q1 == customer.name:
            print ('{}, your current balance is {}'.format(customer.name, currency(int(customer.balance))))
        else:
            print ('Name does not match any account')
            break
        q2 = input ('Enter amount to deposit: ')
        new_balance = customer.balance + int(q2)
        if int(q2) <= 0:
            print('Must deposit amount greater than 0')
        else:
            print('Your balance is now {}'.format(currency(int(new_balance))))
            break

            
def menu():
    print('################ Welcome to Orme Bank ##################')
    main = input('Would you like to Deposit or Withdraw? {}'.format('\n'))
    if main == 'Withdraw':
        withdraw()
    elif main == 'Deposit':
        deposit()
    else:
        print ('Invalid input')


menu()
            
        

        










