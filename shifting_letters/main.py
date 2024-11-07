s = input("Enter the value of s: ")
shifts = []
for i in range(len(s)):
    shifts.append(int(input("Enter value: ")))

alphabets = list('abcdefghijklmnopqrstuvwxyz')
ans = ""

for i in range(len(s)):
    shifts[i] = sum(shifts[i:])

for i in range(len(s)):
    new = (alphabets.index(s[i])+shifts[i])%26
    ans += alphabets[new]
print("The Shifted String is : ",ans)