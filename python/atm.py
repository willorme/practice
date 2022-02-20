from locale import currency
import locale
import time

locale.setlocale(locale.LC_ALL, '')

class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance



customers = [Customer('Amanda Keller', 22, 10000000.00),Customer('Will Orme', 23, 20000000.00)
,Customer('Steve Orme', 26, 25.00)]
    



def menu():
    print('################ Welcome to Orme Bank ##################')
   
    for customer in range(len(customers)):
        
        balance = customers[customer].balance
        name = customers[customer].name

        main = input('Enter your name: ')
        if main == name:
            print ('{}, your current balance is {}'.format(name, currency(float(balance))))
        else:
            print ('Name does not match existing account')
            continue
        wd = input('Would you like to withdraw or deposit? ')



        
        if wd == 'withdraw':

    

            q = input ('Enter amount to withdraw: ')
            new_balance = balance - float(q)
            print('Withdrawing cash...')
            time.sleep(3)
            if float(q) > balance:
                print ('Insufficient funds')
                continue
            else: 
                print('Your balance is now {}'.format(currency(float(new_balance))))
                break

    
            
        elif wd == 'deposit':
            
           

            q = input ('Enter amount to deposit: ')
            new_balance = balance + float(q)
            print('Adding funds to your account...')
            time.sleep(3)
            if float(q) <= 0:
                print('Must deposit amount greater than 0')
                continue
            else:
                print('Your balance is now {}'.format(currency(float(new_balance))))
                break
            

            

        else:
            print ('Invalid input')
        continue



menu()
        










