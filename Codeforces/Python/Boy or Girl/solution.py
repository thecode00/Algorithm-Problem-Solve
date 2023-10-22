# https://codeforces.com/problemset/problem/236/A

string = input()
if len(set(string)) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
