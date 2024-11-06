l = ["RR","GR","RG","GR","GR","RR"]

print("The tiles are : ", l)
GR = RR = RG = GG = 0
for i in l:
    if i == "GR":
        GR += 1
    elif i == "RR":
        RR += 1
    elif i ==  "RG":
        RG += 1
    else:
        GG += 1

if (GR==0 and RG==0):
    print(max(RR,GG))
elif (GR==0 or RG==0):
    print(RR+GG+1)
else: # So both GR and RG greater than 0
    print("The longest possible sequence of tiles are: ",(RR+GG+2*(min(GR,RG)) + (0 if GR-RG==0 else 1)))