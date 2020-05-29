# github repository- Bhavana-B

# python code challenge 01

# Write python code to verify user_name = "Micheal" and password ="e3$WT89x". The total number of attempts are 03. For every wrong user_name and password Print - Invalid username or Password, upon three attempts fails print- Account locked... If inputs are correct Print - You have successfully login





for i in range(1,4):
    u_n = input("Enter username: ")
    pas = input("Enter Password: ")
    if(u_n == 'Micheal' and pas  == 'e3$WT89x' ):
        print("You have successfully login...")
        break
    else :
        print("Invaid username or password...")
        if(i == 3):
            print("Account Locked...")