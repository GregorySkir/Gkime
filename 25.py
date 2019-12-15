names_list = ["foo", "bar", "baz"]
m=len(names_list)
s1 = '' 
count=0
while count<m:
    s1+=names_list[count]
    if count!=m-1:
        s1+=', '
    count+=1
print(s1)