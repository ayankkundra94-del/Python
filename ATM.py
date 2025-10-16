balance=0 
while True:
    print("n\. Deposit") 
    print("2.withdraw") 
    print("3. Check Balance") 
    print("4.Exit") 
    choice=input("Enter your choice:") 
    if choice=='1':
        amount=int(input("enter amount to deposit:")) 
        balance=balance+amount
        print(balance) 
    elif choice=='2':
        amount=int(input("Enter amount to withdrow:"))
        if amount>balance:
            print("Not enough money",balance) 
        else:
            balance=balance-amount
            print("money withdrow",balance) 
    elif choice=='3':
        print("your balance is:",balance) 
    elif choice=='4':
        print("Thank You Bay!") 
        break
    else:
        print("Wrong choise! Try again") 