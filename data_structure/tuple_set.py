s = {2, 4, 5, 100}
s.update(["wasim"])
s.add(101)
print(s)

s.discard(101)
s1 = {'coding', 'hiking', 'reading'}
s2 = {'coding', 'photography', 'travelling'}

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
frozen_set = frozenset(s)
print(frozen_set)
t = ("pwskills", "Ajay", 2, 2.3, True, 3+5j)
print(t.count(2))
print(t.index(2))
t1 = (1, 2, 100, 0, 200)
t2 = (101, 201)

print((t1 + t2))

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 1}

union_set = s1.union(s2)
print(union_set)
intersection_set = s1.intersection(s2)
print(intersection_set)
diff_set = s1.difference(s2)
print(diff_set)
s1.discard(1)
print(s1)
print(s1.difference_update(s2))
print(s1)
print(s1.isdisjoint(s2))