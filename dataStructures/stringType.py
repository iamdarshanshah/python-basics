s="This is my world."
print(s)

s1="""*** 
My world is
not perfect"""

print(s1)

print(s[0])
print(s[3])

# Repeatation of string
print(s*2)

# lenght of string
print(len(s))
print(len(s1))

# Partial/Slice string print [ s = This is my world.]
print(s[0:3]) #Thi
print(s[0:]) #This is my world.
print(s[:8]) #This is
print(s[-3:-1]) #ld

# Slice using step
print(s[0:9:2]) #Ti sm
print(s[17::-1]) #.dlrow ym si sihT
print(s[::-1]) #.dlrow ym si sihT


## Trim the string
s2 = "    dummy    "
print(s2.strip()) #dummy
print(s2.lstrip()) #dummy
print(s2.rstrip()) #    dummy

## Find position of substring in string

s3 = "THis is not a game"
print(s3.find("not")) #8
print(s3.find("not", 0 ,5)) #-1
print(s3.find("not", 7)) #8