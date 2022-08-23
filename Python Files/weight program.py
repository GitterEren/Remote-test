inputt=''
while inputt!='kilograms' and inputt!='pounds':
      inputt=input('Enter with kilograms or pounds:')
      if inputt!='kilograms' and inputt!='pounds':
            print('Wrong input please enter "kilograms" or "pounds" ')


weight=' '
while type(weight)!=float and type(weight)!=int:
      weight=int(input('Please enter your weight:'))
      if type(weight)!=float and type(weight)!=int:
            print('Please enter a float or integer number')


if inputt=='kilograms':
      
      print(f'Your weight is {weight*2.2} pounds')
else:
      print(f'Your weight is {weight/2.2} kilograms')