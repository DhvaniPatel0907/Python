l = []
for i in range(1,31):
    l.append(i)
file = open("test4.txt","w")
file.write(str(l))
file.close()