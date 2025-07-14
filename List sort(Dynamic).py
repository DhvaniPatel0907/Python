l = []
n = int(input("Enter a Length of List: "))
for i in range(1, n + 1):
    n1 = int(input("Enter a Number: "))
    l.append(n1)

print(l)

l1 = len(l)
l.sort()
for i in range(0, l1):
    for j in range(i + 1, l1):
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp



for i in range(0, l1):
    print("ASC Order:", l[i])
