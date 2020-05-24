attempts=0
while attempts<3:
    username=input('enter username:')
    password=input('password:')
    if username=='Micheal'and password=='e3$WT89x':
        print('you are successfully loged in!')
    else:
        attempts+=1
        print('invalid username and password!')
        if attempts==3:
            print('Account locked')

# Code is detecting correct but loop is repeting, so rectify the error.
enter username:jack
jack
password:234
invalid username and password!
enter username:Micheal
Micheal
password:e3$WT89x
e3$WT89x
you are successfully loged in!
enter username:
