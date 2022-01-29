class Customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance



customers = [Customer('Will Orme', '23', str(62500)),
Customer('Amanda Keller', '22', str(10000000))]



def withdraw():
    for customer in customers:
        q1 = input('Enter your name: ')
        if q1 == customer.name:
            print (customer.name + ', your current balance is ' + customer.balance)
        else:
            print ('Name does not match any account')
            break
        q2 = input ('Enter amount to withdraw: ')
        new_balance = int(customer.balance) - int(q2)
        if q2 > customer.balance:
            print ('Insufficient funds')
            break
        else: 
            print('Your balance is now ' + str(new_balance))
            break

def deposit():
    for customer in customers:
        q1 = input('Enter your name: ')
        if q1 == customer.name:
            print (customer.name + ', your current balance is ' + customer.balance)
        else:
            print ('Name does not match any account')
            break
        q2 = input ('Enter amount to deposit: ')
        new_balance = int(customer.balance) + int(q2)
        if int(q2) <= 0:
            print('Must deposit amount greater than 0')
        else:
            print('Your balance is now: ' + str(new_balance))
            break

            
def menu():
    pass 


            
        

        










