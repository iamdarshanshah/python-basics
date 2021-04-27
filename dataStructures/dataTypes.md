# Data types in python - (FIVE)

1. **None** Type - An object that does not contain any value
2. **Numeric** Type - int, float, complex.
3. **Sequences** - string, byte, bytearrya, list, tuple, range
4. **Sets** - Does not allow duplicates
5. **Mappings** - Used in map and reduce

# Collections

## List(array) 
- Can add diff. types of data in list. Slicing and repetition is similar to that of string.
- use `append` and `remove` functions to insert and delete by value resp.
- use `del` to remove values by passing index.
- use `clr` to clear the list.
- use `min|max` to find min and max element in list.
- use `insert` method to insert value at specific index
- use `sort` to sort list in ascending order by default and `sort(reverse=true)` for descending order.
```buildoutcfg
  lst.append(value)
  lst.remove(value)
  del(lst[1])
  lst.insert(3, 55)
  ```

# Tuple
- Just like list data structure.
- Is `immutable`
- Maintains insertion order.
```buildoutcfg
t1=(1,2,3)
t2=1,2,3
```

## Set
- initialized using `{}` braces.
- Cannot store duplicate elements
- Doesn't maintain insertion order.
- Cannot perform indexing, repetition, slice.
- To add elemets use `set.update([e1,e2])`.
- To remove elements use `set.remove(e)`.
- **`Frozen Set`** - Doesn't allow any update or removal of elements from set.
```buildoutcfg
fset = frozenset(set)
```

## Range
- Used to create iterable values that an be used in looping.
- e.g.
```buildoutcfg
# Start form 0 to 5 excluding 5
r = range(5)
for i in r:
    print(i)

r1 = range(1,6)
for i in r1:
    print(i)

r2 = range(1,9,2)
for i in r2:
    print(i)
```

## Dictionary
- Stores values in `key:value` format, initalized using `{}`.
```buildoutcfg
dic1 = {"name": "John", 2: "bob", True: "bill"}

print(dic1)

key = dic1.keys()

values = dic1.values()

for i in key: print(i)

for i in values: print(i)

del dic1[2]
print(dic1)
```
- Note :- deletion happens on the key value provided.