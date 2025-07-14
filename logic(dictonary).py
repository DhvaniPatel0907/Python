d1 = {'p': 1100, 'q': 300, 'r': 600}
d2 = {'p': 400, 'q': 200}
ans = {}
for i,j in d1.items():
    for k,l in d2.items():
        if i == k:
            ans[i]=j+l
print(ans)
