import os
class Phone:
    def __init__(self,phoneNumber,amount):
        self.init_balance = 0

        self.phoneNumber = phoneNumber
        self.amount = amount
        
        
    
    def sms(self):
        """
        NETCATTTT
        """
        amount = self.amount
        number = self.phoneNumber
        balance = self.init_balance + int(amount)
        os.system(f"""echo "You have recieved R{amount} via Ha!
Your new balance is R{balance}

Withdraw at the nearest ATM, Bank or Supermarket" | netcat 172.16.16.241 02114&""")
        # os.system("exit")
        pass
    # def balanceCheck():
    
    


