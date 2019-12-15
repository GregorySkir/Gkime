def replace_key_value(my_dict):
    d={}
    for k, v in my_dict.items():
        d[v]=[]
    for k, v in my_dict.items():
        d[v].append(k)
    return d
print(replace_key_value({'watermelon': 'green', 'pomegranate': 'red', 'peach': 'orange', 'cherry': 'red', 'pear': 'green', 'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}))
