import random as r 

theNumber=r.randint(1,100)
gusses=0
while gusses<5:
    gusses_number=int(input('Enter Your Guss 1-100?'))
    gusses+=1
    if gusses_number==theNumber:
        print(f'You Win The Game in {gusses} Gusses')
        break
    else:
        print('Try Again')