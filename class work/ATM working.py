data={
    1234:{"pin":1224,"current_Balance":5000,"history":[]},
    2345:{"pin":1214,"current_Balance":6000,"history":[]},
    5678:{"pin":1214,"current_Balance":7000,"history":[]}

    }
print("Welcome to the ATM")
acc=int(input("Enter card no: "))
pin=int(input("enter pin: "))
if acc in data and data [acc]["pin"]==pin:
    print("Log in Succussfully")
    while True:
        print('''\n \n ATM MENU
        1.Check Balance
        2.Deposit
        3.Withdraw
        4.View Transactions
        5.Exit''')
        ch=int(input("Enter a choice from (1-5): "))
        if ch==1:
            print(f"current Balance :$ {data[acc]['current_balance']}")
        elif ch==2:
            amount=int(input("Enter amount to deposit: "))
            data[acc]["current_balance"]+=amount
            data[acc]["history"].append(f"Deposited amount $ {amount}")
            print(f"Successfully deposited{amount}")
        elif ch==3:
            amount=int(input("Enter amount to withdraw:"))
            if data[acc]["current_balance"]>=amount:
                data[acc]["current_balance"]-=amount
                data[acc]["history"].append(f"Withdraw {amount}")
                print(f"succussfully withdraw $ {amount}")
            else:
                print("ins blnc")
        elif ch==4:
            print("Transaction History:")   
            for i in data[acc]["history"]:
                print(f"-{i}")
        elif ch==5:
            break
        else:
            print("invalid option")       
else:
    print(" invalid details,try again ")

