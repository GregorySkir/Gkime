'''
def count_vowels(s):
    s = s.casefold()
    l= s.split(" ")
    i=0
    k=0
    l2=[]
    for i in int(len(l)):
        word=l[i]
        for k in len(l[i]):
            if 'a'or 'e'or 'i'or 'o'or 'u' in word:
                l2[i]+=1
    return(l2)
'''
def count_vowels(s):
    l = s.casefold()
    l= s.split()
    z=[]
    e=0
    for word in l:
        x=  l[e].count("a") + l[e].count("i") + l[e].count("e") + l[e].count("o") + l[e].count("u")
        z.append (x)
        e +=1
    return (z)
print(count_vowels("Don't worry, be happy"))