menu = {'Pizza': 200, 'Burger': 150, "Biriyani": 250, "Dosa": 80, "Idly": 50}

print("Menu items are:")
for i in menu:
    print(i, ":", menu[i])

l = []
while(True):
    choice = input("Want to order something? (Yes/No): ")
    if choice.lower() == 'yes':
        prod = input("What do you want to order: ")
        l.append(prod)
    else:
        break

total = 0
for i in l:
    total += menu[i]

if total>500:
    print("You have a discount of 10%")
    total = total*0.9
print("Total amount to be paid is:", total)