def invert_dict(my_dict):
    d={}
    for k, v in my_dict.items():
        d[v]=k
    return d
my_dict = {1: "a", 2:"b", 3:"c"}
print(invert_dict(my_dict))