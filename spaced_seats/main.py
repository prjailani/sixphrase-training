N = int(input("Enter the number of seats: "))
l = []
for i in range(1,N+1):
    l.append(int(input("Enter the alloted value for seat number "+str(i)+": ")))

ans = []

for i in l:
    ans.append(i)
    ans.append(0)
    if i%2==0:
        ans.append(0)

print("The alloted seats are: ",end="")
for i in ans:
    print(i,end=" ")