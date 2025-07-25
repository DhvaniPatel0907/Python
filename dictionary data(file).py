d = {}
for i in range(1, 31):
   d[i]=i*i

file = open("test3.txt", "w")
file.write(str(d))
file.close()
