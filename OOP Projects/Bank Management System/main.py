from User_interface import user_interface
from Admin_inter_face import admin_interface

print("1.Admin Interface")
print("2.User Interface")
print("3.Exit")

while True:
    choice = int(input("Select Option 1/2 Pick 3 To Exit : "))

    if choice == 1:
        admin_interface()

    elif choice == 2:
        user_interface()

    elif choice == 3:
        break 

    else:
        print("Please Choise Correct Option")   
