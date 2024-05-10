import time
print("Please insert your card")
time.sleep(5)
password=1234
pin=int(input("enter your atm pin"))
balance=5000
if pin==password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit""")
        try:
            option=int(input("enter your choice:"))
        except:
            print("please enter valid option")
        if option==1:
            print(f"Your current balance is {balance}")
            print("==================================================================")
            print("==================================================================")
            print("===================================================================")
        if option==2:
            withdraw_amount=int(input("Please enter withdraw amount"))
            print("==================================================================")
            print("==================================================================")
            print("===================================================================")

            balance=balance-withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print("==================================================================")
            print("==================================================================")
            print("===================================================================")
            print(f"your current balance is {balance}")
        if option==3:
            deposit_amount=int(input("Please enter deposit amount"))
            print("==================================================================")
            print("==================================================================")
            print("===================================================================")
            balance=balance+withdraw_amount
            print(f"{deposit_amount} is credited to your account")
            print("==================================================================")
            print("==================================================================")
            print("===================================================================")
            print(f"your current balance is {balance}")
        if option==4:
            exit


else:
    print("wrong pin Please try again")