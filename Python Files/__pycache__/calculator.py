def calculator():
    print('Calculations are done from first umber to second number.')
    First_number=float(input('Enter first number: '))
    Second_number=float(input('Enter second number: '))
    print('4 options \n1.Add \n2.Substitute \n3.Multiplication\n4.Division')
    tupl=('Add','Substitute','Multiplication','Division')
    request=input(('Which one do you want'))
    while request not in tupl:
        print('The desired request is not appropriate for this program. Please choose one of the top.')
        request=input(('Which one do you want'))
         
    if request==tupl[0]:
         print(First_number + Second_number)
         return 
    if request==tupl[1]:
        print(First_number - Second_number)
        return 
    if request==tupl[2]:
        print(First_number * Second_number)
        return First_number * Second_number
    if request==tupl[3]:
        print(First_number / Second_number)
        return 
    