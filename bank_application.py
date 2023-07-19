class transaction:
    def __init__(self,a):
        self.a=a
    def withdraw(self):
        c=50000-self.a
        print("Your available balance is:- ",c)
    def deposit(self):
        c=50000+self.a
        print("Your available balance is:- ",c)
        
class login:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def login(self):
        if self.a=='user' and self.b=='user123':
            print("You are logged in!!!")
            print("""
                  ========================================
                  1.Withdraw
                  2.Deposit
                  ========================================
                  """)
            d=int(input(" Select your choice:- "))
            if d==1:
                a=int(input("Enter amount to withdraw:- "))
                c=transaction(a)
                c.withdraw()
            elif d==2:
                a=int(input("Enter amount to deposit:- "))
                c=transaction(a)
                c.deposit()
        else:
            print("Log in failed!!!")


print("""
==========================================
                  Bank
==========================================     
      """)
a=input("Username:- ") 
b=input("Password:- ")

c=login(a,b)
c.login()

        
