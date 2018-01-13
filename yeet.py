print ("Chicken simulator yeet")
name1 = input('what be your name player1')
name2 = input ('what be your name player2')

boof21 = input('type anything to continue')

print (name1 + " you are driving head on into another car, do you swerve or keep going")
player1 = input("type swerve or forwards")
if player1 == 'swerve' or player1 == 'forwards':
    print ('yeet')
else:
    print ('type swerve or forwards ' + name1)

boof22 = input('type anything to continue')


print (name2 + " you are driving head on into another car, do you swerve or keep going")
player2 = input("type swerve or forwards")
if player2 == 'swerve' or player2 == 'forwards':
    print ('yeet')
else:
    print ('type swerve or forwards' + name2)

boof = input('type anything to continue')

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