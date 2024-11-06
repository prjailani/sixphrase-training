n = int(input("Enter a number: "))
l = []

for i in str(n):
    l.append(int(i))
l.sort(reverse=True)
ans = 0

length = len(l)-1
for i in l:
    ans += i*(10**length)
    length -= 1
print(ans)