from Users import Admin
from bank_object import bank

def admin_interface():
    option = input("Login Or Register ! l/r : ").lower()
    if option == 'r' and len(bank.admin) == 1:
        option = 'l'
        print("Admin Already Exit Need To l\n")

    if option == 'r':
        name = input("Enter Your Name : ")
        email = input("Enter Your Email : ")
        address = input("Enter Your Address : ")
        account_type = input("Enter The Type Of Account : ")
        password = input("Enter Your Password : ")
        ad = Admin(name=name, email=email, address=address, account_type=account_type, password=password)

        while True:
            print("1. Delete Any User Account")
            print("2.Show All User Account List")
            print("3.Check The Total Available Balance Of The Bank")
            print("4.Check The Total Loan Amount")
            print("5.On Or Off The Loan Feature Of The Bank")
            print("6.Main Menu")
            print("7.Add Money To The Bank")
            
            choice = int(input("Choice Any Option : "))
            
            if choice == 1:
                id = int(input("Enter The User Id"))
                ad.delete_user(bank, id)

            elif choice == 2:
                ad.see_all_user_account_list(bank)

            elif choice == 3:
                ad.show_bank_balance(bank)

            elif choice == 4:
                ad.show_total_loans_amount(bank)

            elif choice == 5:
                Set = bool(input("Enter Ture Or Flase To On Or Off Loan Feature : "))
                ad.set_loan_status(bank, Set)

            elif choice == 6:
                break

            elif choice == 7:
                money = int(input("Enter The Amount : "))

            else:
                print("Please Chooce The Correct Option : ")

    
    elif option == 'l':
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        ad = bank.valid_user_or_not(email, password)

        if ad:
            while True:
                print("1.Delete Any User Account")
                print("2.Show All User Accounts List")
                print("3.Check The Total Available Balance Of The Bank")
                print("4.Check The Total Loan Amount")
                print("5.On Or Off The Loan Feature Of The Bank")
                print("6.Main Manu")
                print("7.Add Money To The Bank")
                choice = int(input("Choice The Option : "))
                if choice == 1:
                    id = int(input("Enter The User Id"))
                    ad.delete_user(bank, id)
                
                elif choice == 2:
                    ad.see_all_user_account_list(bank)

                elif choice == 3:
                    ad.show_bank_balance(bank) 

                elif choice == 4:
                    ad.show_total_loans_amount(bank)

                elif choice == 5:
                    Set = bool(input("Enter Ture Of Flase To On Or Off Loan Feature"))
                    ad.set_loan_status(bank, Set)

                elif choice == 6:
                    break

                elif choice == 7:
                    money = int(input("Enter The Amount"))
                    bank.add_money(money)

                else:
                    print("Please Chooce The Correct Option")

        else:
            print("The Admin Not Exist!!!")

    else:
        print("Sorry You Need To Chooice l Of r!!!")
