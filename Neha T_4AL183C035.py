attempts=0
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
# Your code is able to verify correctly but even after successful login again it is asking to provide the details, so rectify the bug
Enter your usernameMicheal
Enter your passworde3$WT89x
You are successfully logged in
Enter your username
