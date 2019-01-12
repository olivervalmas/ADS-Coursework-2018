from itertools import permutations

num = 123
print(set(int(''.join(p)) for p in permutations(str(num))))