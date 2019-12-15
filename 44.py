def print_value(dic):
    for i in dic:
        print ("The value of {} is: {}".format(i, dic.get(i)))
dic={"red":"color", "cat":"animal"}
print_value(dic)