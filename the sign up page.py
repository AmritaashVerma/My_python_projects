from getpass import getpass

sign_up = input ("Enter the login id you want over here: ")
password = getpass("Enter your password over here: ")
print ("Are you sure you want to continue with this login id: " + sign_up + "\nAnd this password: " + password)
response = input ("yes or no(y = yes, n = no)? ")
if response in ["y", "Y"]:
    print ("You have successfully created an account!!!")
elif response ["n", "N"]:
    sign_up = input ("Enter login id over here: ")
    password = getpass("Enter password here: ")
    print ("Are you sure now that you want to have this login id: " + sign_up + "\nAnd this password: " + password)
    response = input ("yes or no(y = yes, n=no)? ")
else:
    print("Error 400: Bad response!")

if response in ["Y", "y", " y", " Y"]:
    print ("You have succesfully made an account(again)!!!")
else:
    print ("Nothing can be done of such an unsure and loser person! I can't help you anymore!")
