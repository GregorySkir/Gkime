#q3
def delwords(s, li):
    strsplit=s.split(" ")
    newstr=''
    for i in range(len(li)):
        while strsplit.count(li[i]) != 0:
            strsplit.remove(li[i])
    for i in range(len(strsplit)):
        newstr+=strsplit[i] + ' '
    print(newstr)
delwords('Hello Hello World jjj fff kkk', ['Hello','jjj'])