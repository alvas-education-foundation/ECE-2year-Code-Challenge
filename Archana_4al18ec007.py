i=0

while(i<=3):
    if (i == 3):
        print("account locked")
        exit(0)
    name=input("enter user_name")
    passw=input("enter the password")
    if(name!="Micheal" or passw!="e3$WT89x"):
        print("invalid user_name or Password")

    else:
        print("you have successfully login")
        exit(0)
    i+=1
