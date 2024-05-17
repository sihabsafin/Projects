from Users import User
from bank_object import bank

def user_interface():
    option = input("Login Or Register ? l/r : ").lower()

    if option == 'r':
        name = input("Enter Your Name : ")
        email = input("Enter Your Email : ")
        address = input("Enter Your Address : ")
        account_type = input("Enter Your Account Type : ")
        password = input("Enter Your Password : ")
        us = User(name=name, email=email, address=address, account_type=account_type, password=password)
        
        while True:
            print("1.Deposit Money")
            print("2.Withdrow Money")
            print("3.Show Balance")
            print("4.Check Transection History")
            print("5.Transfer Money")
            print("6.Main Menu")

            choice = int(input("Enter The Option : "))

            if choice == 1:
                money = int(input("Enter The Deposit Amount : "))
                us.deposit(bank, money)

            elif choice == 2:
                amount = int(input("Enter The Amount For Withdrow : "))
                us.withdrow(bank, amount)

            elif choice == 3:
                us.show_balance()

            elif choice == 4:
                us.check_history()

            elif choice == 5:
                id = int(input("Enter The Account Id : "))
                amount = int(input("Enter The Amount : "))
                us.transfar_money(bank, id, amount)

            elif choice == 6:
                break

            else:
                print("Please Chooice Correct Option!!!")

    elif option == 'l':
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        us = bank.valid_user_or_not(email, password) 

        if us:
            while True:
                print("1.Deposit Money")
                print("2.Withdrow Money")
                print("3.Show Balance")
                print("4.Check Transection History")
                print("5.Transfer Money")
                print("6.Main Menu")

                choice = int(input("Enter The Option : "))

                if choice == 1:
                    money = int(input("Enter The Deposit Amount : "))
                    us.deposit(bank, money)

                elif choice == 2:
                    amount = int(input("Enter The Amount For Withdrow : "))
                    us.withdrow(bank, amount)

                elif choice == 3:
                    us.show_balance()

                elif choice == 4:
                    us.check_history()

                elif choice == 5:
                    id = int(input("Enter The Account Id : "))
                    amount = int(input("Enter The Amount : "))
                    us.transfar_money(bank, id, amount)

                elif choice == 6:
                    break

                else:
                    print("Please Chooice Correct Option!!!")

        else:
            print("Sorry You Give Wrong Information")

    else:
        print("Sorry You Need To Chooice l Of r!!!")               
                                

