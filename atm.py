balance=0
mini_statement=[]

def credit():
    global balance
    amount=float(input("enter amount to credit:"))
    if amount<=0:
        print("please enter the positive amount.")
    else:
        balance+=amount
        mini_statement . append(f"creadited:${amount}")
        print(f"${amount}creadited to your account.")


def debit():
   global balance

   amount=float(input("enter amount to debit:")) 
   if amount<=0:
      print("please enter positive amount.")
   elif amount > balance:
      print("insufficient balance.")
   else:
        balance-=amount
        mini_statement . append(f"debited:${amount}")
        print(f"${amount} debited from your account.")

def check_balance():
    print("\n-----mini statement-----")

    if len(mini_statement)==0:
       print("no transactions found.")

    else:
        for i in mini_statement:
            print(i)
    print(f"available balance:${balance}")

def menu():
    while True:
        print("\n ATM MENU")
        print("1. credit")
        print("2. debit")
        print("3. balance")
        print("4. mini statement")
        print("5. exit")

        choice=input("enter your choice(1-5):")
        if choice=='1':
           credit()
        elif choice=='2':
            debit()
        elif choice=='3':
            check_balance()
        elif choice=='4':
            show_mini_statement()
        elif choice=='5':
            print("Thank You for using the ATM.Goodbye!")
            break
        else:
            print("Invalid choice. please try again.")
menu()
             
         

