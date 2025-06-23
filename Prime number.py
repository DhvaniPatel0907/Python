n = int(input("Enter a Number:"))
if n<0:
    print("Enter Positive Number")
else:
    if n==1 or n==3 :
        print("Prime")
    else:
        prime=0
        for i in range (1,n+1):
            if(n%i==0):
                prime+=1
        if prime==2:
                print(n,"Is Prime")
        else:
                print(n,"Is Not Prime")