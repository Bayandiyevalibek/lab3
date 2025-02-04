from itertools import permutations

def print_permutations(s):
    unique_perms = set(permutations(s))  
    for p in unique_perms:
        print(''.join(p))
