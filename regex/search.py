import re

str = "take up one idea.One idea at a time"

result = re.search(r'o\w\w', str)  # one
result = re.search(r'o\w', str)    # on

print(result.group())
