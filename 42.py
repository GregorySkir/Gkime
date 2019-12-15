def remove_duplicate (x):
    z= []
    for a in x:
        if a in z:
            continue
        else:
            z.append(a)          
    return z
my_list = "the player went to the stadium".split()
print(remove_duplicate(my_list))