def count_occurrences(s):
    l=s.split()
    d={}
    for i in l:
        v= l.count(i)
        d[i]=v
    return d
print(count_occurrences("dog cat cat dog mouse dog"))