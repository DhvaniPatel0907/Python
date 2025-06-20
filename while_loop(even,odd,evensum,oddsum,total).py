i = 1
ev = 0
od = 0
evsum = 0
odsum = 0
total_sum = 0
while i <= 3:
    n = int(input("Enter a Number: "))
    if n % 2 == 0:
        print(n, "even")
        ev += 1
        evsum += n
    else:
        print(n, "odd")
        od += 1
        odsum += n

    total_sum += n  
    i += 1         

print("Even Count:", ev)
print("Odd Count:", od)
print("Even Sum:", evsum)
print("Odd Sum:", odsum)
print("Total Sum:", total_sum)
