#q2b
def devii(n=int(input("Enter the number:\n")), d=int(input("Enter the devide number:\n"))):
    for i in range(int(n)+1):
        if i%d==0:
            print(i)

devii()