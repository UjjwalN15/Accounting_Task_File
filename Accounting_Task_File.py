import json
import time
import random
import os
def main():
    while True:
        print ("Enter 1 for login\nEnter 2 for register\nEnter 3 for exit.")
        try:
            choice = int(input("Enter your choice: "))
            time.sleep(1)
            os.system("cls")
        except ValueError:
            print("You have entered the wrong choice. Please entered a valid choice.")
            time.sleep(3)
            os.system("cls")
            continue
        if choice == 1:
            login()
            time.sleep(2) 
        elif choice == 2:
            register()
            time.sleep(2)
            
        elif choice == 3:
            again()
        else:
            print("You have entered the wrong choice.Please try again.")
            time.sleep(1)
            continue

def login():
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_data.txt","r")
    except FileNotFoundError:
        open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_data.txt","w").close()
    user_data = data_file.read()
    data_file.close()
    if user_data == "":
        print("No data in the database.Please register to continue.")
        register()
    else:
        login_username = input("Enter your login username: ")
        login_password = input("Enter your login password: ")
        list_user_data = user_data.split("-")
        login = False
        for i in list_user_data:
            if i != "":
                dict_user_data = json.loads(i)
                if login_username in dict_user_data and dict_user_data.get(login_username) == login_password:
                     login = True 
                     break
                time.sleep(2)
        if login :
            print(f"Login successful.Hello {login_username}")
            Accounting(login_username)
        else:
            
            print("Invalid Credentials.")
def register():
    register_username = input("Enter your register username: ")
    if register_username.isdigit():
        time.sleep(1)
        print("Username cannot be only number.")
        register()
    elif register_username == "":
        time.sleep(1)
        print("Username cannot be empty.")
        register()
    register_password = input("Enter your register password: ")
    if register_password == "":
        time.sleep(1)
        print("Password cannot be empty.")
        register()
    elif len(register_password) < 6:
        time.sleep(1)
        print("Password must be at least 6 characters")
        register()
    try:
        data_file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_data.txt","r")
    except FileNotFoundError:
        open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_data.txtt","w").close()
    user_existing_data = data_file.read()
    data_file.close()
    list_user_existing_data = user_existing_data.split("-")
    for datas in list_user_existing_data:
        if datas != "":
            dict_user_existing_data = json.loads(datas)
            if register_username in dict_user_existing_data:
                time.sleep(1)
                print("Username already exists")
                register()
    if register_username.isdigit():
        time.sleep(1)
        print("Username cannot be only number.")
        register()
    elif register_username == "":
        time.sleep(1)
        print("Username cannot be empty.")
        register()
    else:
        while True:
            captcha = random.randint(1000,9999)
            print("The captcha is ",captcha)
            try:
                captcha_input = int(input("Enter the captcha: "))
            except ValueError:
                time.sleep(1)
                print("Please enter the mentioned captcha.")
                time.sleep(1)
                continue
            if captcha == captcha_input:
                time.sleep(2)
                user_data = {register_username:register_password}
                json_user_data = json.dumps(user_data)
                file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_data.txt", "a")
                file.write(json_user_data + "-")
                file.close()
                user_balance_data = {register_username : "0"}
                json_user_balance_data = json.dumps(user_balance_data)
                file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_balance_data.txt", "a")
                file.write(json_user_balance_data + "-")
                file.close()
                time.sleep(2)
                print(f"Registration Successful with the username {register_username}")
                main()
            else:
                time.sleep(1)
                print("Please enter the valid captcha.")
                time.sleep(1)
                continue
def Accounting(username):
    time.sleep(1)
    print("Enter 1 to check balance\nEnter 2 to add balance\nEnter 3 to withdraw balance\nEnter 4 to exit")
    try:
        user_accounting_choice = int(input("Enter your choice: "))
    except ValueError:
        time.sleep(1)
        print("You entered a wrong choice.Please try again.")
        Accounting(username)
    if user_accounting_choice > 4:
        time.sleep(1)
        print("Please enter a valid choice. Please try again.")
        Accounting(username)
    elif user_accounting_choice == 1:
        time.sleep(1)
        Check_balance(username)
    elif user_accounting_choice == 2:
        time.sleep(1)
        Add_balance(username)
    elif user_accounting_choice == 3:
        time.sleep(1)
        Withdraw_balance(username)
    elif user_accounting_choice == 4:
        time.sleep(1)
        again()
    else:
        time.sleep(1)
        print("Please enter a valid choice. Please try again.")
        Accounting(username)
def Check_balance(username):
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_balance_data.txt", "r")
    balance_data = file.read()
    file.close()
    list_balance_data = balance_data.split("-")
    balance = 0
    for datas in list_balance_data:
        if datas != "":
            dict_balance_data = json.loads(datas)
            if username in dict_balance_data:
                balance += int(dict_balance_data.get(username))
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_Withdraw_data.txt", "r")
    withdraw_record = file.read()
    file.close()
    list_withdraw_record = withdraw_record.split("-")
    for i in list_withdraw_record:
        if i != "":
            dict_withdraw_record = json.loads(i)
            if username in dict_withdraw_record:
                balance -= int(dict_withdraw_record.get(username))
    print("Calculating . . . . . .")
    time.sleep(1)
    print(f"Your balance is {balance}.")
    Accounting(username)
def Add_balance(username):
    time.sleep(1)
    add_balance = int(input("Enter the balance to add to your account: "))
    add_balance_data = {username : add_balance}
    json_add_balance_data = json.dumps(add_balance_data)
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_balance_data.txt", "a")
    file.write(json_add_balance_data+"-")
    file.close()
    time.sleep(1)
    print(f"{add_balance} Successfully added in your account.\n")
    Accounting(username)
    
def Withdraw_balance(username):
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_balance_data.txt", "r")
    balance_data = file.read()
    file.close()
    list_balance_data = balance_data.split("-")
    balance = 0
    for datas in list_balance_data:
        if datas != "":
            dict_balance_data = json.loads(datas)
            if username in dict_balance_data:
                balance += int(dict_balance_data.get(username))
    file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_Withdraw_data.txt", "r")
    withdraw_record = file.read()
    file.close()
    list_withdraw_record = withdraw_record.split("-")
    for i in list_withdraw_record:
        if i != "":
            dict_withdraw_record = json.loads(i)
            if username in dict_withdraw_record:
                balance -= int(dict_withdraw_record.get(username))
    print("Calculating . . . . . .")
    time.sleep(1)
    print(f"Your balance is {balance}.")
    user_withdraw_balance = int(input("Enter the balance to withdraw: "))
    if balance < user_withdraw_balance:
        time.sleep(1)
        print(f"{user_withdraw_balance} cannot be withdrawn because of insufficient balance.")
        Accounting(username)
    elif user_withdraw_balance == 0:
        time.sleep(1)
        print(f"{user_withdraw_balance} cannot be withdrawn.")
        Accounting(username)
    elif user_withdraw_balance < 1000:
        time.sleep(1)
        print("The minimun amount threshold to withdraw is RS.1000.")
        Accounting(username)
    else:
        user_withdraw_data = {username:user_withdraw_balance}
        json_user_withdraw_data = json.dumps(user_withdraw_data)
        file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_Withdraw_data.txt", "a")
        file.write(json_user_withdraw_data + "-")
        file.close()
        time.sleep(1)
        print(f"{user_withdraw_balance} Successfully withdrawn.")
        file = open("C:/Users/prajw/OneDrive/Desktop/Python Programming/Accounting_Task_File/Accounting_Task_User_Withdraw_data.txt", "r")
        withdraw_balance = file.read()
        file.close()
        list_withdraw_balance = withdraw_balance.split("-")
        for i in list_withdraw_balance:
            if i != "":
                dict_withdraw_balance = json.loads(i)
                if username in dict_withdraw_balance:
                    balance -= int(dict_withdraw_balance.get(username))
        time.sleep(1)
        print(f"Your current balance is {balance}.")
    Accounting(username)
           
    
    
def again():
    time.sleep(1)
    while True:
        again = input("Do you want to use the system again?(y/n) : ").lower()
        if again == "n":
            exit(0)
        if again == "y":
            time.sleep(1)
            time.sleep(1)
            main()
        else:
            time.sleep(1)
            print("You have to enter either y or n. Thank you.")
            time.sleep(1)
            continue
        
main()