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

