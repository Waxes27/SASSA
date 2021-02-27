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
        os.system(f'echo "You have recieved {amount} via Ha!\nYour new balance is R{balance}" | netcat 172.16.1.69 0544&')
        pass
    


