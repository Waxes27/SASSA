import datetime
import phone1
import phone2
import os

"""
Roll out, Adoptions
"""
balance = 1800

print("Welcome to HA!\n")

def identification():
    ID = input("Please enter 13-Digit ID number: ")
    while len(ID) != 13:
        ID = input("Please enter 13-Digit ID number: ")

    age = "".join(list(ID)[0:2])

    current_year = int(str(datetime.date.today()).split('-')[0])

    if list(age)[0] == '0':
        age2 = list(age)[1]
        age = 2000 + int(age2)

    new_age = current_year - int(age)
    if len(list(str(new_age))) == 4:
        new_age = "".join(list(str(new_age))[2:])

    with open('storage.txt','r+') as file_:
        for i in file_.readlines():
            print(i.split('-'))
            if i.split("-")[0] == ID:
                os.system("clear")
                pinVerify = input("Please enter your PIN: ")
                print(i.split('-')[2])
                print(f"Welcome {ID}\n\nYour balance is: R{balance}\n")
                options()
                exit(0)
        
        pin = input("Please set your 5-digit pin E.g. (12345): ")
        file_.write(f"{ID}-{balance}-{pin}\n")
        print("Registering...")
        print("Successfully registered...Please come back.")
        exit()

def options():
    print("Here are your available options:\n\n1. Pay\n2. Withdraw\n3. Link Bank Account\n")
    pass



def login_():
    print("Welcome...\n")
    options = int(input("1. Login\n2. Redeem\n\n"))
    os.system("clear")
    if options == 1:
        identification()        

login_()
