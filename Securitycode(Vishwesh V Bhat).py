#Objective: WAP to verify Username and Password, Username = 'Micheal' and Password = 'e3$WT89x', and with just 3 attempts for the user.

user_name = "Micheal"
user_input = input("Enter username : ".upper())
    if user_input == user_name:
        for Attempts in range(3):
          password = 'x'
          pas_input = input("Enter password : ".upper())
          if pas_input == password:
            print("You have successfully logged in!!!".upper())
            break
          else:
            print("Wrong Password!!")
        else:
            print("Account locked!!")  
            
            
    else:
      print("wrong Username!!")

 
