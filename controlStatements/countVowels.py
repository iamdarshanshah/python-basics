word = input("Enter the word :: ")

vowels = {'a','e','i','o','u'}

vowelDictionary = {}

for c in word:
    if c.lower() in vowels:
        vowelDictionary[c] = vowelDictionary.get(c,0)+1

print(vowelDictionary)