'''
#exe1
users = ['Nathan',2313,'Geez','pass231','Abebe','092313133','Miki',"pl3s34D0n'tH4ckM3"]
x = users[0:9:2]
y = users[1:9:2]
print (f"The Usernames Are: {x}")
print (f"The Usernames Are: {y}")
'''
#exe2
users = {'Nathan':2313,'Geez':'pass231','Abebe':'092313133','Miki':"pl3s34D0n'tH4ckM3"}
print( f"Your password is: {users[input("Enter USERNAME: " )]}")

'''
#exe3
number = int(input("Enter No: "))
if number % 2 == 0:
    print(f"{number} is even no.")
else:
    print(f"{number} is odd no.")
'''