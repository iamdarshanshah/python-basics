# Even or odd

num = int(input("Enter a number :: "))

if num == 0:
    print("{} is Zero".format(num))
elif num % 2 == 0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))
