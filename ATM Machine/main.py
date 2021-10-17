print("Wlecome to the Test bank ATM\n")
balance = 990.0
chance = 3
while chance >0:
    pin = int(input("Enter your 4 digit pin "))
    if pin == (1234) :
        print("\nPress 1 for balance enquiry \nPress 2 for withdrawl \nPress 3 for Deposit \nPress 4 for Exit")

        try:
            option = int(input("Please enter your choise "))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"Your current balance is {balance}")
            exit()

        elif option == 2:
            withdraw_amount = int(input("please enter withdraw_amount "))
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account")
            print(f"your updated balance is {balance}")
            break

        elif option == 3:
            deposit_amount = int(input("please enter deposit_amount "))
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account")

            print(f"your updated balance is {balance}")
            break
        elif option == 4:
            print("Thank You")
            exit()
        else:
            print("Sorry something went wrong. Please try again")
            break

    elif pin != ('1234'):
        print("Incorrect password")

    chance = chance-1

if chance == 0:
    print("You have no tries left")
    exit()

print("\nThank you for being transcation with us!")