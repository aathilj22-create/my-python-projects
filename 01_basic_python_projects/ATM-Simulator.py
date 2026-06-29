balance = 5000

print("Welcome to the ATM Simulator!")

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = int(input("Enter your choice (1-4): "))
    
    if choice == 1:
        print(print("Your current balance is: Rs.", balance))
        
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print("Successfully deposited Rs.", amount)
            print("New Balance is Rs.", balance)
        else:
            print("Invalid amount!")
            
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance! You don't have enough money.")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance = balance - amount
            print("Successfully withdrawn Rs.", amount)
            print("Remaining Balance is Rs.", balance)
            
    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please select between 1 and 4.")