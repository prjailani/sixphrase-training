N = int(input("Enter the number of numbers you're going to write on the board: "))
arr = []
for i in range(N):
    arr.append(int(input("Enter a number: ")))
count = 0

initial = arr[0]%2

for i in range(1,len(arr)):
    if arr[i]%2 != initial:
        count += 1
        initial = arr[i]%2
print("Total swithces required: ",count)