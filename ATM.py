import time
import getpass

print("Please insert your card")
time.sleep(2)

password = 1234
balance = 5000

try:
    pin = int(getpass.getpass("Enter your ATM PIN: "))
except ValueError:
    print("Invalid PIN format. Exiting...")
    exit()

if pin == password:
    while True:
        print("""
        ====== ATM MENU ======
        1. Check Balance
        2. Withdraw
        3. Deposit
        4. Exit
        =======================
        """)
        try:
            option = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if option == 1:
            print(f"Your current balance is ₹{balance}")

        elif option == 2:
            try:
                withdraw_amount = int(input("Enter amount to withdraw: ₹"))
                if withdraw_amount > balance:
                    print("Insufficient funds.")
                elif withdraw_amount <= 0:
                    print("Withdrawal amount must be positive.")
                else:
                    balance -= withdraw_amount
                    print(f"₹{withdraw_amount} withdrawn. New balance: ₹{balance}")
            except ValueError:
                print(" Invalid input. Please enter a number.")

        elif option == 3:
            try:
                deposit_amount = int(input("Enter amount to deposit: ₹"))
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    balance += deposit_amount
                    print(f"✅ ₹{deposit_amount} deposited. New balance: ₹{balance}")
            except ValueError:
                print(" Invalid input. Please enter a number.")

        elif option == 4:
            print(" Exiting... Thank you for using our ATM!")
            break

        else:
            print(" Please choose a valid option (1-4).")
else:
    print("Incorrect PIN. Access denied.")
