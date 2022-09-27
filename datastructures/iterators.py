## Itertools python: product, permutations, combinations, accumulate, groupby, infinite iterators

from itertools import product, permutations, combinations, accumulate, groupby
import operator

# Product
a = [1,2,3]
b = [3,4]
prod = product(a, b) # cartesian product of iterables. returns iterator object
print(f"Product: {list(prod)}")

## Permutations: orderings of an input
perm = permutations(a, 3)
print(f"PERMUTATIONS: {list(perm)}")

## Combinations: possible combinations of an input
comb = combinations(a, 2)
print(f"COMBINATIONS: {list(comb)}")

##accumulate: 
a = [1,2,3,4]
acc = accumulate(a) #default computes running sums
acc_mul = accumulate(a, func=operator.mul) # cummulative products
print(f"Accumulator: {list(acc)}, {lists(acc_mul)}")
