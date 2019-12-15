def words_lengths(s1):
    li1=s1.split()
    i=0
    l2=[]
    while i < len(li1):
        l2.append(len(li1[i]))
        i+=1
    return (l2)
print(words_lengths('This is a test'))