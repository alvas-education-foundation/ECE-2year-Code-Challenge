print('Enter correct username and password to continue')
count=0
while count<3:
    username=input('Enter username:')
    password=input('Enter password:')
    
    if password=='e3$WT89x' and username=='Micheal':
        print('You have successfully login')
        break
        
    else:
        count+=1
        print('Invalid username or Password')
        
    if count==3:
        print('Account locked')
