import re

str = "take up one idea.one idea at a time"

result = re.findall(r'o\w\w', str)

print(result)  # ['one', 'one']

result = re.match(r'o\w\w', str)  # Only works with start of the string

print(result.group())  # None
