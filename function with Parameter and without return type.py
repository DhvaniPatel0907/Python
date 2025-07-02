def prime(n):                        #Parameter
    prime = 0
    for i in range (1,n+1):
        if n%i==0:
            prime+=1
    if prime == 2 or prime==3 :
        print("Prime")
    else:
        print("Not Prime")
prime(7)                              #arguments