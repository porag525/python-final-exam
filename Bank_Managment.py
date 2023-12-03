class User:
    account_num=5000
    def __init__(self, username, initial_balance,mobile,pin,email):
        self.username = username
        self.balance = initial_balance
        self.ac_num=User.account_num
        self.mobile=mobile
        self.email=email
        self.pin=pin
        self.transaction_history = []
        self.loan_limit = 2 * initial_balance
        self.loan_taken = 0
        User.account_num +=1
    def __repr__(self) -> str:
        print(f'Account Name : {self.username}')
        print(f'Mobile Number :{self.mobile}')
        print(f'Balance : {self.balance}')
        return "Thank You"
    
    #  Deposit Done 
    def deposit(self,amount):
        
        if amount>0:
            self.balance += amount
            print(f'Your transaction is completed.Current Balance = {self.balance}')
            self.transaction_history.append(f"Deposited ${amount}")
        else :
            print("Invalid Amount.Deposite Aborted")
            
    #  Withdraw Done
    def withdraw(self,amount):
        
        if amount <= self.balance:
            self.balance -= amount
            print(f'Transaction Completed. Current Balance = {self.balance}')
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds. Cannot withdraw.")

    # Transfer Done
    def transfer(self, recipient):
        amount=int(input("Enter the balance to transfer : "))
        if amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to {recipient.username}")
        else:
            print("Insufficient funds. Cannot transfer.")

    # Check balanc Done
    def check_balance(self):
        return self.balance

    # Take loan Done
    def take_loan(self,amount,status):
        
        if status==True:
            if amount <= self.loan_limit - self.loan_taken:
                 self.loan_taken += amount
                 self.deposit(amount)
                 self.transaction_history.append(f"Loan taken: ${amount}")
            
            else:
                print("Loan limit exceeded.")
    
    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.balance and amount > 0:
            self.balance      = self.balance - amount
            other.balance     = other.balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.balance}')
            self.transaction_history.append(f'Money Transfer : $ {amount}')
        else:
            print('Invalid amount transaction aborted')
        
        

    # Transaction History Done
    def check_transaction_history(self):
        print(self.transaction_history)


class Admin:
    
    user=[]
    balance=int(100000)
    loan=0
    def users(self):
        print(f'Total Customer is = {len(self.user)}')
    def create_Admin(self, username,mobile,pin):
        self.admin_name=username
        self.mobile=mobile
        self.pin=pin

    def check_total_balance(self):
           
        print(f'Total Balance is = {self.balance} ')

    def check_total_loan(self):
        print(f'Total given loan is = {self.loan}')

    def toggle_loan_feature(self, enable):
        if(self.balance<50000):
            User.loan_enabled=False
        User.loan_enabled = enable
    


customer_dict = {}              # use account no. as key and class object(customer account) as value
mobile_acc_link = {}   # use mobile no. as key and store account no. as value, for linking purpose
porag=Admin()
sami=User("Sami",29489,"018",3333,"kfj@gmail.com")
porag.balance+=sami.check_balance()
customer_dict[sami.ac_num] = sami                 # acct. no. stored as key and oject as value
mobile_acc_link[sami.mobile] = sami.ac_num   

porag.user.append(sami)
def Admin_pannel():
    porag.create_Admin("Moniruzzaman Porag","01814622024",2042)
    porag.check_total_balance()
    porag.check_total_loan()
    porag.users()
    

def new_cust():
    name = input('Enter the name of customer: ')
    mobile = int(input('Enter the mobile number of customer: '))
    initial_depo = int(input('Enter the initial deposit amount: '))
    porag.balance+=initial_depo
    email=input("Enter the email  :")
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer =User(username=name, mobile=mobile,initial_balance=initial_depo, pin=pin,email=email)
    porag.user.append(customer)
    customer_dict[customer.ac_num] = customer                 # acct. no. stored as key and oject as value
    mobile_acc_link[customer.mobile] = customer.ac_num     # mobile no. linked
    print('New User Created!')
    print(f'Welcome {customer.username} to Corporate Bank. {customer.ac_num} is your account number')

def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin :
        print(f'\n{customer_dict[account_no].username} Logged in')
        print(customer_dict[account_no])
    else:
        print('Account either not exist or the pin is wrong')
        return
    
    while True:
        user_input1 = input('''Press 1 for deposit:
Press 2 for withdrawl:
Press 3 for money transfer:
Press 4 for see transactions:
Press 5 to Take loan
Prss 6 to Logged out\n''')
        if user_input1 == '1':
            amount=int(input("Enter the deposite amount : "))
            porag.balance+=amount
            customer_dict[account_no].deposit(amount)
        elif user_input1 == '2':
            amount=int(input("Enter the Withdrawal amount : "))
            porag.balance-=amount
            customer_dict[account_no].withdraw(amount)
        elif user_input1 == '3':
            mobile =(input('Enter the mobile number of recepient: '))
            if mobile in mobile_acc_link.keys():
                secondary = mobile_acc_link[mobile]             # use mobile no. to get acct. no.
                customer_dict[account_no].payment(customer_dict[secondary])
            else:
                print('The mobile number you have enter does not have an account associated with it')
        elif user_input1 =='4':
            customer_dict[account_no].check_transaction_history()
        
        elif user_input1 =='5':
            amount=int(input("Enter the Loan amount : "))
            porag.balance-=amount
            porag.loan+=amount
            customer_dict[account_no].take_loan(amount,True)   
            
        elif user_input1 == '6':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        print(customer_dict[account_no])

print("----------------------------------------------------------------")
print("  $$$$$$$$$$$$$$$$$ BANK MANAGMENT SYSTEM $$$$$$$$$$$$$$$$$$  ")
print("----------------------------------------------------------------")
while True:
    user_input1 = input('''Press 1 for creating a new customer:
Press 2 for logging in as an existing customer:
Press 3 for displaying number of customers:
Press 4 for Log in as an Admin
Press 5 for exit\n''')

    if user_input1 == '1':
        print('Create user')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print('There currently', User.no_of_cust,'customers in Corporate bank.')
    elif user_input1 == '4':
        print("Logged in as a admin")
        Admin_pannel()
    elif user_input1=='5'  :
        exit()
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')