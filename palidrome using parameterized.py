def fun1(s):
    

    rev = s[::-1]
    if s == rev:
      print(f"'{s}' is a palindrome.")
    else:
      print(f"'{s}' is not a palindrome.")
s = input("Enter a word: ")
fun1(s)
