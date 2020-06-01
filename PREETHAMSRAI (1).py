total_attempt=0
while total_attempt<3:
           username=input(“enter your user name: ”)
           password=input(“enter your password ”)
           If username==’Michal' and password==’e3$WT89x':
                  print(“you are successfully loged in")
          else:        
                 print(“you entered wrong login id. Please check again\n”)  
                 print(‘you have’ ,3-total_attempt)   
                total_attempt+=1
                if total_attempt==3:
                   print(“account blocked")
