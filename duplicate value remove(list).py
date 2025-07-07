l = []
n = int(input("Enter a Length of List: "))
for i in range(1, n + 1):
    n1 = int(input("Enter a Number: "))
    l.append(n1)


print(l)
l1=[]

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)