def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac

n = int(input("Enter a number: "))
print(factorial(n))