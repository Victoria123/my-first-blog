print('Hello, Django girls!')
if 3>2:
    print ('It works!')
    if 5>2:
       print('5 is indeed greater than 2')
    else:
       print('5 is not greater than 2')
name='Sonja'
if name=='Ola':
     print ('Hey Ola!')
elif name=='Sonja':
     print('Hey Sonja!')
else:
     print ('Hey anonymos!')
def hi():
    print('Hi there!')
    print('How are you?')
hi()
def hi(name):
    if name=='Ola':
        print('Hi Ola!')
    elif name=='Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymos!')
hi('Vicky') 
def hi(name):
    print('Hi ' + name + '!')
hi('Rachel')
girls= ['Rachel', 'Monica','Phoebe','Ola']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1,6):
    print(i)
name = 'Marta'
if name=='Ola':
    print('Hey Ola!')
elif name== 'Sonja':
    print ('Hey Sonja!')
elif name== 'Vicky':
    print('Hey Vicky')
else:
    print('Hey you!')

    
    
    


    
    
        

       