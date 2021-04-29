## List comprehensions

- shortcut way of creating a list from another while applying logic on items of another iterable along with using some condition
```buildoutcfg
l = [ expression for item in iterable if condition]
```
- e.g. - Even numbers in a list

```buildoutcfg
lst = [x for x in range(2,21,2)]
print(lst)

----------------------------------------------

lst = [x for x in range(2,21) if x% % 2 == 0]
print(lst)
```