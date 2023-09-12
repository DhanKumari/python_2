import datetime
import pytz



class Account:
    
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)
    
    def __init__(self, name , balance):  #init = initialise 
        self._name=name
        self.__balance=balance
        self._transaction_list=[(Account._current_time(), balance)]
        print("account created for "+ self._name)
        self.show_balance()
        
    def deposit(self, amount):  #new method
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(),amount))

    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("amount must be greater")
        self.show_balance()
            
    def show_balance(self):
        print("balance is {}".format(self.__balance))
        
    def show_transaction(self):
        for date, amount in self._transaction_list:
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
    
    steph = Account("steph", 800)
    steph.__balance= 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    steph.show_balance()
    print(steph.__dict__)
    
  
        
    