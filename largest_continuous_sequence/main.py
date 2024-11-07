N = int(input("Enter the number: "))
l = []
for i in range(N):
    l.append(int(input("value "+str(i)+": ")))

ans = []
def seq(l):
    if (sum(l))==0:
        ans.append(l)
        return l
    seq(l[1:])
    seq(l[:-1])

seq(l)

m = len(max(ans))

for i in ans:
    if len(i)==m:
        print("Largest Continuous Sequence: ",i)
        break