l = [32,98,76,56,41]
l1=len(l)
l.sort()
for i in range(0,l1):
    for j in range(i+1,l1):
        if(l[i]<l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
for i in range(0,l1):
    print("DEASC order:",l[i])