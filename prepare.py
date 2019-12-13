def palin(s=input("write string!\n")):
    if s==s[::-1]:
        print('Yes', s[::-1])
    else:
        print('No')
palin()