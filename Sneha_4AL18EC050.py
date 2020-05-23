attempt=0
while attempt<3:
    user_name=input("Enter the username: ")
    password =input("Enter the password :")
    if user_name =="Micheal" and password =="e3$WT89x":
            print("You have successfully logged in")
    else:
            attempt+1
            print("Invalid username or password")
 print("Account Locked")
