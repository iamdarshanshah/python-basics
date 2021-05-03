print("Welcome to myWay Sandwiches.")

toppingsDictionary = {1: "Onion", 2: "Lettuce", 3: "Tomato", 4: "Olives", 5: "Pepper"}

print("Available Toppings are")

for eachKey in toppingsDictionary.keys():
    print(eachKey, ":: ", toppingsDictionary.get(eachKey))

toppingSelected = []

for i in range(1,4):
    a = input("Select {}st topping :: ".format(i))
    toppingSelected.append(int(a))

print("Selected toppings :")

for eachTopping in toppingSelected:
    print(toppingsDictionary.get(eachTopping))

sandwichCount = int(input("Units of sandwich :: "))

print("Total bill at $5 per sandwich :: ${}".format(5*sandwichCount))



