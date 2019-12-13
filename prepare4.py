def countpets(heads, legs):
    for i in range(heads):
        j=heads-i
        if (2*i)+(4*j)==legs:
            return i,j
print(countpets(35,94))