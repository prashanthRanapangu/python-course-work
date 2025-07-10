#set creation Syntax
myset={1,2,3,4,}
empty_set=set()
set_with_duplicate={1,2,3,4}
print(set_with_duplicate) #{1,2,3,4}
my_set={1,2,3,4,5}
print(3 in my_set)     #True
print(6 not in my_set) #True

set1={1,2,3,4}
set2={3,4,5,6}
print(set1 | set2)   #{1, 2, 3, 4, 5, 6}
print(set1 & set2)    #{3,4}
print(set1-set2)    #{1,2}
print(set1.difference(set2))   #{1,2}
print(set1^set2)      #{1, 2, 5, 6}
print(set1<=set2)      #false
print(set1.isdisjoint(set2))  #false
(set1.add(6))
print(set1)
set1.remove(6)
print(set1)         #{1, 2, 3, 4}
set1.discard(7)
print(set1)          #{1, 2, 3, 4}
set2.pop()
print(set2)           #{4, 5, 6}
set_with_duplicate.clear()
print(set_with_duplicate)    #set)
#Bulit in Functions for sets
print(len(set1))     #4
print(max(set1))     #4
print(min(set1))     #1
print(sorted(set1))  #[1, 2, 3, 4]

frozen=frozenset([1,2,3,4])
print(frozen)         #frozenset({1, 2, 3, 4})
