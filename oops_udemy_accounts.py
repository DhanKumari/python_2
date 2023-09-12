import datetime
import pytz



class Account:
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name , balance):  #init = initialise 
        self.name=name
        self.balance=balance
        self.transaction_list=[]
        print("account created for "+ self.name)
        
    def deposit(self, amount):  #new method
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(),amount))

    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("amount must be greater")
        self.show_balance()
            
    def show_balance(self):
        print("balance is {}".format(self.balance))
        
    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount >0:
                tran_type = "depositor"
            else:
                tran_type = "withdraw"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone))
        
        
if __name__ == '__main__':
    kannu = Account("kannu",0)
    kannu.show_balance()
    
    kannu.deposit(1000)
    #kannu.show_balance()
    kannu.withdraw(200)
    
    kannu.withdraw(1000)
    
    kannu.show_transaction()
    
    steph = Account("steph",800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    
  
        
    