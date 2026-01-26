# create set
sets = {"sanjana", 22, 2, 3, 3}
print(type(sets))        # <class 'set'>
print(sets)              # duplicates removed

# 1 add() – add single element
sets.add(455)
print(sets)              # element added

# 2 update() – add multiple elements
sets.update([10, 20])
print(sets)

# 3 remove() – removes element (error if not found)
sets.remove(22)
print(sets)

# 4 discard() – removes element (no error)
sets.discard(100)
print(sets)

# 5 pop() – removes random element
sets.pop()
print(sets)

# 6 clear() – removes all elements
temp = {1, 2, 3}
temp.clear()
print(temp)              # set()

# 7 union() – combine sets
a = {1, 2}
b = {2, 3}
print(a.union(b))        # {1,2,3}

# 8 intersection() – common elements
print(a.intersection(b)) # {2}

# 9 difference() – elements in a not in b
print(a.difference(b))   # {1}

# 10 symmetric_difference() – uncommon elements
print(a.symmetric_difference(b)) # {1,3}

# 11 issubset() – check subset
print({1}.issubset(a))   # True

# 12 issuperset() – check superset
print(a.issuperset({1})) # True

# 13 isdisjoint() – no common elements
print(a.isdisjoint({4,5})) # True

# 14 copy() – copy set
c = a.copy()
print(c)

# 15 len() – number of elements
print(len(a))            # 2
