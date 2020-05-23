correct = True
while correct:
    name = input("what is the user_name?")
    if name == "micheal".lower():
        password = input("please enter your password: ")
        if password == "e3$WT89x":
            print("you have successfully login.")
            break

        if password != "e3$WT89x":
            passwordi = input("invalid password,would you like to try user_name and password again?y/n: ")
            if passwordi == "y".lower():
                correct = True
            correct=0:
                 while count < 3:
                    print("invalid password.")
                else:
                    print("account blocked.")
            correct+=1
            break

            else:
                print("thank you for trying to login,goodbye. ")
                quit()

    if name != "micheal".lower():
        username = input("username incorrect,would you like to try the username again?y/n: ")
        if username == "y".lower():
            correct == True
        else:
            print("thankyou for trying to login")
            quit()