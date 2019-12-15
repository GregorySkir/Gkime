import string
letters = string.ascii_lowercase
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    i+=1
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    j-=1
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    j-=1
    i+=1
