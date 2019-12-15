import random
def guess_my_number_again(num=None, tries=5):
    t=0
    if num==None:
        num=random.randint(1,100)
    while t<tries:
        num2=random.randint(1,100)
        if num2>num:
            print('too high')
        elif num2<num:
            print('too low')
        else:
            return(num2, t, True)
            break
        t+=1
    if t==tries:
        return(num,t,False)
guess_my_number_again()
