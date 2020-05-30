username = 'Polly1220'

password = 'Bob'

userInput = input("What is your username?\n")
a = input("Password?\n")
count = 1
i=0
while count < 3:
        if userInput == username and a == password:
            print("login successful")
        if userInput != username or a != password:
          print("your username and password is incorrect\ntry again")
          count += 1
          i += 1
          user=input("\nusername\n")
          pas=input("\npassword\n")
          if user == username and pas == password:
           print("login succesful after wrong attempts",i)
           break
          if user != username or pas != password :
           print("your username and password is incorrect\ntry again")
           count += 1
           i += 1
           user=input("\nusername\n")
           pas=input("\npassword\n")
          if user == username and pas == password:
           print("login succesful after wrong attempts",i)
           break
          if user != username or pas != password :
             print("your username and password is incorrect\ntry again")
             count += 1
             i += 1
             user=input("\nusername\n")
             pas=input("\npassword\n")
             if user == username and pas == password:
              print("login succesful after wrong attempts",i)
              break
             if user != username or pas != password :
              print("your username and password is incorrect\ntry again")
              count += 1
              i += 1 
                         
if count == 3:
 print("3 wrong attempts, ACCOUNT BLOCKED")

        