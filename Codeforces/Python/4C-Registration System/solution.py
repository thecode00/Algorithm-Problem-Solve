"""
https://codeforces.com/problemset/problem/4/C
Time complexity: O(N)
"""

import sys

input = sys.stdin.readline

database = {}
for _ in range(int(input())):
    name = input().strip()
    if name not in database:
        print("OK")
        database[name] = 1  # Store number for when name already exist
    else:
        new_name = name + str(database[name])
        database[new_name] = 1
        print(new_name)
        database[name] += 1
print(database)
