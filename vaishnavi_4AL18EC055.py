username=input("enter username")
key=input("enter password")
count=0
user="Micheal"
password="e3$WT89x"
while count<3:
 if key==password and username==user:
  print("login successful")
 else:
  print("invalid credentials")
  
  # your code is entering in to infinite loop when the credentials are wrong. so fix the bug.
