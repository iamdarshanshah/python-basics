# Remove duplicates from a given list

lst = [1,1,4,5,88,92,88,334,4]

print(set(lst))

# Enter a list as input (Using eval)

lst = eval(input("Enter list of elements :: "))
print(lst)

## Remove duplicates without using set
lstUniq = []
for eachValue in lst:
    if eachValue not in lstUniq:
        lstUniq.append(eachValue)

print(lstUniq)