L1 = list(range(1,6))
L2 = ['five', 'four', 'three', 'two', 'one']
L1.append('six')
L1.extend(L2)
print(L1)
m = L1.index(5)
L1.remove(5)
n = L1.index('five')
L1.remove('five')
L1.insert(m,'five')
L1.insert(n+1,5)
print(L1[0:len(L1):2])