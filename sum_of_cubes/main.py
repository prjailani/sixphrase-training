m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

sum = 0
for i in range(m,n+1):
    sum += i**3
print("Sum = ",sum)