import datetime
import phone
import os
import random
import json
import time

"""
Roll out, Adoptions
"""

balance = 1800

file_ = open('storage.json','r+')

user_dict = {}

print("Welcome to HA!\n")

def identification():
    global file_
    ID = input("Please enter 13-Digit ID number: ")
    while len(ID) != 13 or not ID.isdigit():
        ID = input("Please enter '13-Digit' ID number: ")

    age = "".join(list(ID)[0:2])

    current_year = int(str(datetime.date.today()).split('-')[0])

    if list(age)[0] == '0':
        age2 = list(age)[1]
        age = 2000 + int(age2)

    new_age = current_year - int(age)
    if len(list(str(new_age))) == 4:
        new_age = "".join(list(str(new_age))[2:])
    
    file_ = json.load(file_)
    try:
        if file_['id'] == ID:
            pinverify = input("please enter your pin: ")
            os.system("clear")
            
            counter = 3
            while file_['pin'] != pinverify:
                pinverify = input("please re-enter your pin: ")
                counter = counter - 1
                if counter == 0:
                    print("this account has been locked due to security please reactivate the account")
                    exit()
            else:
                print(f"welcome {ID}\n\nyour balance is: R{balance}\n")
                options()
                exit(0)
    except FileExistsError:
        pass

        

    pin = input("please set your 5-digit pin e.g. (12345): ")
    while len(pin) != 5 or not pin.isdigit():
        pin = input("please set a valid 5-digit pin e.g. (12345): ")

    user_dict['id'] = ID
    user_dict['balance'] = balance
    pin2 = input("Please re-enter your pin: ")
    if pin == pin2:
        user_dict['pin'] = pin
    user_dict['linked'] = False

    print(user_dict)
    userinfo = json.dumps(user_dict, indent=4)
    file_.write(userinfo)
    print("registering...")
    print("successfully registered...please come back.")
    exit()



def options():
    global file_
    option = int(input("""Here are your available options:\n
    1. Pay
    2. Withdraw
    """))
    os.system("clear")
    if option == 1:
        pay(file_)
    elif option == 2:
        withdraw(file_)
    # elif option == 3:
    #     link(file_)
    

def link(file_):
    print("Linking...")
    pass


def pay(file_):
    phoneNumber = input("Please enter phone number to pay: ")
    phoneNumber2 = input('Please re-enter the phone number to pay: ')

    amountToSend = input("Amount you would like to pay: ")

    if phoneNumber == phoneNumber2:
        test = phone.Phone(phoneNumber,amountToSend)
        test.sms()
        time.sleep(3)
        print(f"User has been paid\n\nYour new balance is: R{balance-int(amountToSend)}")
    pass



def withdraw(file_):
    # print("Withdrawing...")
    
    pass



def login_():
    global file_
    print("Welcome...\n")
    options = int(input("1. Login\n2. Redeem\n3. Exit\n>> "))
    os.system("clear")
    if options == 1:
        identification()
    elif options == 2:
        withdraw(file_)
        # print("Redeeming...")
        a = random.randint(1000,9999)
        print(f"Your OTP is {a}")
    return options

option = 0
while option != 3:
    option = login_()
os.system("clear")
print("Ha!..\n\nCome again soon")
