correct_pin="123"
balance=10000
attempt=0
maximum_attempt=3
transactions=[]
# login functionality

while True:
    enter_pin=input("enter you pin: ")
    if enter_pin==correct_pin:
        print("pin is verified successfully")
        break
    else:
        attempt=attempt+1
        print("incorrect pin, Attempts left",maximum_attempt-attempt)
        if maximum_attempt==attempt:
            print("your atm card is blocked due to limit exeeds")
            exit()

# core function
while True:
    print("...... Main Menu ......")
    print("enter 1 to check your balance")
    print("enter 2 to deposit money")
    print("enter 3 to withdraw money")
    print("enter 4 to know mini statement")
    print("enter 5 to exit")

    # to check balance
    choice =input("enter your choice: ")
    if choice=="1":
        print(f"your balance is {balance}")
    elif choice=="2":
        d_amount=int(input("enter amount for deposit : "))
        if d_amount>0:
            balance=balance+d_amount
            transactions.append(f"deposite : {d_amount}")
            if len(transactions)>5:
                transactions.pop(5)
            print("deposite is successful,your new balance is : ",balance)
        else:
            print("invalid amount")
    elif choice=="3":
        w_amount=int(input("enter amount to withdraw : "))
        if w_amount>0 and w_amount<=balance:
            balance=balance-w_amount
            transactions.append(f"withdrwa : {w_amount}")
            if len(transactions)>5:
                transactions.pop(5)
            print("withdraw is successful,your new balanceis : ",balance)
        else:
            print("invalid balance")
    elif choice=="4":
        print("previous transactions are : ")
        if len(transactions)==0:
            print("no transactions done till now")
        else:
            for t in transactions:
                print(t)
    elif choice=="5":
        print("thank you for using this ATM ")
        break
    else:
        print("invalid choice")
        
        
        
