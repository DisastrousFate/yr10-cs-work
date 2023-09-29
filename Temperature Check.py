import random

lowerThan15 = 0
higherThan20 = 0

firstTemp = int(input("Enter temperature: "))
print("The other 364 temperatures will be randomised..")

tempList = []
tempList.append(firstTemp)
for x in range(364):
    tempList.append(random.randint(5,30))

for element in tempList:
    if element < 15:
        lowerThan15 += 1
    if element > 20:
        higherThan20 += 1

print("Lower than 15: "+str(lowerThan15))
print("Higher than 20: "+str(higherThan20))


