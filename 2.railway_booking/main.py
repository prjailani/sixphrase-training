quantity = int(input("How many tickets you want to book? : "))
sum = 0
for i in range(quantity):
    age = int(input("Enter the age of person " + str(i+1) + " : "))
    if age > 60:
        sum += 30
    elif age < 12:
        sum += 20
    else:
        sum += 50
print("Total amount to be paid: ",sum)