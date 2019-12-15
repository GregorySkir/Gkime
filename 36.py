def guess_my_number(num):
    while True:
        num2=int(input('guess the number 1-100'))
        if num2>num:
            print('too high')
        elif num2<num:
            print('too low')
        else:
            return(num,'congratulation')
            break
guess_my_number(37)