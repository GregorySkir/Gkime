def my_range(n, f="", k=1):
    l=[]
    if f=="":
        f=n
        n=0
    if k >= 0:
        while f > n:
            l.append (n)
            n += k
        return l    
    else:
        while f < n :
            l.append(n)
            n += k
        return l
print(my_range(7))