def me(x,y):
    if x == y:
        print("Logged in successfully!!".upper())
    else:
        print("Wrong password try again!!".upper())

for attempts in range(3):
   a = 'Micheal'
   b = input("Enter username :".upper())
   x = 'abcd2000'
   y = input("Enter password :".upper())
   if a == b:
       me(x,y)
       if x == y:
           print("You Successfully logged in!!")
           break
   else:
       print("The username and password don't match!!! Try again please.")
