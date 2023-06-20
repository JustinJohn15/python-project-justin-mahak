#### creating a class atm
class atm:
    def __init__(self,name):                                  #### accepting the name using a function
        self.name=name
    def acc_info(self):                                       #### taking the function for account information
        print('Account Information: ')
        print('Name: ', name, end='\n')
        print('Account Number: ', info[name][0], end='\n')
        print('Phone Number: ', info[name][1], end='\n')
    def pin_change(self):                                       ####taking the function for pin number and checking for 3times
        i=3
        while(i>0):                                             #### using while loop for checking  for the pin number
            p=int(input('Enter Original PIN: '))
            if p==info[name][2]:
                x=input('Enter New PIN: ')
                info[name][2]=x
                break
            else:
                i=i-1
                print('PIN incorrect, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
    def acc_balance(self):                                              #### using function for account balance of the customer
        print('Account Balance: ',info[name][3])
    def withdraw(self):                                                 #### using function for withdrawing the amount of cash from bank
        print('Account Balance: ',info[name][3])
        amt=float(input('Enter Amount To Be Withdrawn: '))
        if amt<=info[name][3]:
            info[name][3]=info[name][3]-amt
            print('New Account Balance is : ', info[name][3])
        else:
            print('Insufficient Balance in Account!')
    def deposit(self):                                                  #### using function for depositing the money in bank
        amt=float(input('Enter Amount To Be Deposited: '))
        info[name][3]=info[name][3]+amt
        print('New Account Balance: ', info[name][3])

##### ACCEPTING THE INFO FROM THE USER
info={"JUSTIN":[4612485411,123454562,4545,12000.00], "MAHAK":[3769845253,1234567895,8989,10000.00], 'Vedant':[4324567890,1122334455,1234,100000.00], "RONIL":[6669857142,12345677412,1111,17000.00], "VARDHAN":[7779848475,123458481,7777,10500.00]}
k=info.keys()
#### NOW PERFORMING THE ATM FUNCTIONS:-
while (1):
    name=str(input('Enter Name: '))
    if name in k:
        i=3
        while(i>0):
            pin=int(input('Enter PIN: '))  #### if the pin is right the the following functions appear
            if pin==info[name][2]:
                a=atm(name)
                while(1):
                    print('Enter 1 For Account Info')
                    print('Enter 2 For PIN Change')
                    print('Enter 3 For Balance Inquiry')
                    print('Enter 4 For Withdrawal')
                    print('Enter 5 For Deposit')
                    s=int(input('Select Operation: '))
                    if s==1:
                        a.acc_info()
                    elif s==2:
                        a.pin_change()
                    elif s==3:
                        a.acc_balance()
                    elif s==4:
                        a.withdraw()
                    elif s==5:
                        a.deposit()
                    else:
                        print('Invalid Option Selected! Choose Again')
                        continue
                    e=input('Enter Y to exit, press any other key to continue operations: ')  #### for exiting
                    if e=='y' or e=='Y':
                        print('Thank You!')
                        break
                    else:
                        continue
                break
            else:
                i=i-1
                print('Incorrect PIN, {} tries left'.format(i))
        if i==0:
            del info[name]
            print('Account Blocked!')
        break
        ### program end