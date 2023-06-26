
#message = 'a'
#while message != 'secret':
 #   message = input("Enter Password ")
  #  print(message + "Password not correct")

#while True:
 #   message = input("Enter Password ")
  #  if message == 'secret':
  #      break
 #   print(message + " Password not correct")
#print(message + " is your password")
msg = 'a'
mylist = []
while msg != 'stop'.upper():
    msg = input('Enter new item and stop to finish')
    mylist.append(msg)
print(mylist)
