class Account:
    def __init__(self,name,balance=500):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return f'name: {self.name} \nBalance: {self.balance}'

    def withdrawal(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f'\n*ERROR* Your balance is {self.balance}$')
            
    def deposit(self,amount):
        self.balance += amount

class ATM(Account):
    def __init__(self,name,balance=500):
        super().__init__(name,balance)
    
    def ask(self):
        while True:
            try:
                action = str(input('Which action do you want to do? \n\t1. Withdraw \n\t2. Deposit \n\n'))
            except:
                print('Please enter a valid answer.')
                continue
                
            else:
                if action.lower()[0] == 'w' or action.lower()[0] == '1':
                    while True:
                        try:
                            action_two = int(input(f'\nHow many dollars do you want to withdraw? \n--Enter a number between 1 and {self.balance}-- \n\n'))
                        except:
                            print('\nPlease enter a valid answer.')
                            continue
                        else:
                            if action_two <= self.balance:
                                print(f'\n{action_two}$ has successfully been debited from your account \n--> Your new balance is {self.balance - action_two}$')
                                myAccount.withdrawal(action_two)
                            else:
                                print('**Insufficient funds')
                                continue
                        break
                            
                elif action.lower()[0] == 'd' or action.lower()[0] == '2':
                    while True:
                        try:
                            action_three = int(input(f'\nHow many dollars you want to deposit? \n\n'))
                        except:
                            print('\nPlease enter a valid answer.')
                            continue
                        else:
                            myAccount.deposit(action_three)
                            print(f'\n{action_three}$ has successfully been credited on your account \n--> Your new balance is {self.balance}$ \n')
                            break
                            
                else:
                    print('\nPlease enter a valid answer.')
                    continue
                break

myAccount = ATM('Maxime',500)

myAccount.ask()