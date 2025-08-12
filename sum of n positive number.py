

n = int(input("Enter how many numbers: "))

total = 0

for i in range(1, n + 1):
    num = int(input(f"Enter positive number {i}: "))
    if num > 0:
        total += num
    else:
        print("Only positive numbers are allowed!")

print("Sum of positive numbers is:", total)
