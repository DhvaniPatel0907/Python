n = int(input("Enter a Number:"))
with open("test2.txt","w") as f:
    for i in range(1,n+1):
        f.write(str(i))