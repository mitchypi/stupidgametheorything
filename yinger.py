import random
op = ['ichikawa','yinghui','miguel']
choice = ['swerve','forwards']
name2 = random.choice(op)
print ("Chicken simulator yeet")
name1 = input('what be your name player1\n')
print ("your opponent today is " + name2)
boof21 = input('type anything to continue\n')

print (name1 + " you are driving head on into another car, do you swerve or keep going")
player1 = input("enter swerve or forwards\n")
while player1 not in ("forwards", "swerve"):
    player1 = input("Please enter 'swerve' or 'forwards'\n")
boof22 = input('type anything to continue\n')


print (name2 + " is choosing now")
player2 = random.choice(choice)

boof = input('type anything to continue\n')

print(name1 + ' chose ' + player1 + '!')
print(name2 + ' chose ' + player2 + '!')

if player1 == 'swerve' and player2 =='swerve':
    print ('Both ' + name1 + ' and ' + name2 + ' are chickens!')
elif player1 == 'forwards' and player2 =='swerve':
    print (name1 + ' is an alpha and ' +name2 + ' is a chicken')
elif player2 == 'forwards' and player1 == 'swerve':
    print(name2 + ' is an alpha and ' + name1 + ' is a chicken')
elif player1 == 'forwards' and player2 =='forwards':
    print ('both ' + name1 + ' and ' + player2 + ' died!')
else:
    print ('something broke lol')