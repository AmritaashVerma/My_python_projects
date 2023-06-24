import time

def show_password():
    acc_pass = open("password_manager.txt", "r")
    content = []
    for char in acc_pass.readlines():
        char = char.replace('\n', '')
        content.append(char)
    account = input("Enter the name of your account: ")
    found = False
    for index, word in enumerate(content):
        if word == account:
            print("The password to", account, "is", content[index+1])
            found = True
        acc_pass.close()
    if found == False:
        print("There was no password found for the account", account)

def add_password():
    acc_pass = open("password_manager.txt", "a")
    acc = input("Enter the name of your account: ")
    passw = input("Enter the password of ur account: ")
    print("Do you confirm?\nAccount name: ", acc, "\nPassword: ", passw, "\npress ctrl+c to re enter.")
    time.sleep(6)
    acc_pass.write("\n" + acc + "\n")
    acc_pass.write(passw + "\n ")
    print("The account and password have been successfuly added to the manager.")
    acc_pass.close()

def change_password(old, new_acc, new_pass):
    acc_pass = open("password_manager.txt", "r+")
    data = acc_pass.readlines()
    found = False
    for i, char in enumerate(data):
        if old in char:
            data[i] = new_acc
            data[i+1] = new_pass
            found = True
    acc_pass.close()
    if found == True:
        acc_pass = open("password_manager.txt", "w")
        acc_pass.write(''.join(data))
        acc_pass.close()
        print("Your account/password or both have been edited.")
    else:
        print("The account you were looking for is not there. :(")

print("Hello this is a password manager.")
opinion = input("Would you like to see a password(s) or add a password and account(a)\
or change an account or password(c) or remove a password(r): ")
if opinion in ['s', 'S']:
    show_password()
elif opinion in ['a', 'A']:
    add_password()
elif opinion in ['c', 'C']:
    change_password(input("Enter the name of ur old account: "),
    input("Enter the name of ur new account: ") + "\n",
    input("Enter the name of ur new password: ") + "\n")
elif opinion in ['r', 'R']:
    change_password(input("Enter the name of ur the account you want to remove: "), '', '')
else:
    print("Error 400: Bad Request.")
