# Looping Statements

## While

```buildoutcfg
while <Conditions>:
    <Statements>
```

## For

- Used to iterate over a list of elements
- e.g. - list, tuple, set, range, string, frozenSet, dictionaryKeys, dictionaryValues
```buildoutcfg
for <var> in <sequence>:
    stetements
```

## Break and Continue

- Use `break` and `continue` keywords in loop to break out of the loop or to continue with next iteration respectively based on some conditions.

## Assert

- Use `assert` to validate elements in the program.
```buildoutcfg
x = int(input("Enter number greater than 10 :: "))
assert x>10, "X is less than 10"
print("You entered {}".format(x))
```