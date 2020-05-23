attemps=0
while attempts<3:
   username=input('Enter your username')
   password=input('Enter your password')
   if username=='Micheal' and password=='e3$WT89x':
      print('You are successfully logged in')
   else:
        attempts+=1
        print('Invalid username and password')
        if attempts==3:
           print ('account locked')
