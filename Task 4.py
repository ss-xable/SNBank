import random
import sys

# Writing staff details. 
staff_details = open('staff.txt', 'w')
staff_details.write("Username1: jsmith\n")
staff_details.write("Password1: Qwerty12\n")
staff_details.write("Email1: johnsmith@yahoo.com\n")
staff_details.write("Fullname1: John Smith\n\n")

staff_details.write("Username2: dstinson\n")
staff_details.write("Password2: Query12\n")
staff_details.write("Email2: dorcasstinson@yahoo.com\n")
staff_details.write("Fullname2: Dorcas Stinson\n")
staff_details.close()

#The staff login page of the program. 
yes = True
while yes:
    print("=====================================")
    print(" ----   Welcome to SNBank ----       ")

    choice = input("Please select your preferred option: [Yes] for Staff Login [No] to Close App: ").upper()
    start = True
    while start:
        if choice == 'YES':
            
#Reading the staff.txt file. 
            staff_details = open('staff.txt', 'r')
            staff_username = str(input('Enter username: '))
            staff_password = str(input('Enter password: '))

            if staff_username == 'jsmith' and staff_password == 'Qwerty12':
                print("Login Successful!")
                start = False
                yes = False
                print()


            elif staff_username == 'dstinson' and staff_password == 'Query12':
                print()
                print("Login Successful!")
                start = False
                yes = False
                print()


            else:
                print()
                print("Wrong username or password. Please try again")
                staff_username = str(input('Enter username: '))
                staff_password = str(input('Enter password: '))
                start = True

                staff_details.close()
        else:
            sys.exit()
#Creatng Session file.

    choice = True
    while choice:
        session_file = ('session.txt', 'w')

        login_successfully = int(input(
            "Please select your preferred option:" "\n1. To Create New Bank Account" "\n2. To Check Account Details" "\n3. To Logout \n=> "))

#Creating new bank account
        if login_successfully == 1:
            account_name = str(input('Enter Account Name: ')).lower()
            account_balance = str(input('Enter Opening Balance: '))
            account_type = str(input('Account Type: '))
            account_email = str(input('Account Email: '))

#Creating account number
            account_number = ''.join((map(str, [random.randint(1, 9) for i in range(0, 10)])))
            print()
        
#Writing customer details.
            customer_details = open('customer.txt', 'w')
            customer_details.write("Account Name: %s \n" % account_name)
            customer_details.write("Opening Balance: %s \n" % account_balance)
            customer_details.write("Account Type: %s \n" % account_type)
            customer_details.write("Account Email: %s \n" % account_email)
            customer_details.write("Account Number: %s \n" % account_number)
            customer_details.close()

            customer_details = open('customer.txt', "r")
            print(f'Here are your details:\n{customer_details.read()}\n')
            customer_details.close()
            choice = True

#To check account number            
        if login_successfully == 2:
            check = True
            while check:
                account_number1 = (input('Enter Account Number: '))

                if account_number1 == account_number:
                    customer_details = open('customer.txt', "r")
                    print(f'\nHere are your details:\n{customer_details.read()}\n')
                    customer_details.close()
                    check = False
                    choice = True

                else:
                    print('Please input valid account number')
                    print()
                    check = True

#To log out.                     
        if login_successfully == 3:
            print()
            choice = False
            yes = True

        # while open_app == "NO":
        # print("Session ended!")
        # staff_details.close()
