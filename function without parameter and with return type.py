#Factorial

def fun3():
    n = int(input("Enter a Number:"))
    fac=1

    for i in range(1,n+1):
        fac*=i
    return fac
print(fun3())
