lstNum = [int(x) for x in input("Enter list of numbers ::").split()]
count = sum = 0

for num in lstNum:
    sum+=num
    count+=1

print(sum/count)
