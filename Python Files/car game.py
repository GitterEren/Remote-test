starting_text='Car started.. Ready to go'
stopping_text='Car has stopped'
# quitting_text=
input1=input('>')
if input1=='help':
         print('start- to start the car \nstop- to stop the car \nquit- to exit')
dict1=('start','stop','quit')
input2=''
while input2 != 'quit':
    input2=input('>')
    if input2 not in dict1:
        print('I dont understand ...')
    if input2 == 'start':
         print(starting_text)
    elif input2 == 'stop':
        print(stopping_text)
    