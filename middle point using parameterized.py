def fun1(s):
    if len(s)%2==0 :
        print(s)
    else:
        mid = len(s) //2
        print(s[mid-1]+s[mid]+s[mid+1])
s = input("Enter a word: ")
fun1(s)
    
    