# https://codeforces.com/problemset/problem/71/A

n = int(input())
for _ in range(n):
    string = input()
    length = len(string)
    if length > 10:
        print(string[0] + str(len(string) - 2) + string[-1])
    else:
        print(string)
