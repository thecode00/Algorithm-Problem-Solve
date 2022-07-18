# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())
if n % 2 == 0:
    # When n is even amount of even, odd number is same: n // 2
    if n // 2 >= k:
        print(1 + 2 * (k - 1))
    else:   # If k bigger than amount of odd number print even number
        print(2 + 2 * (k - n // 2 - 1))
else:
    # When n is odd number amount of even number: n // 2, odd number: n // 2 + 1
    if n // 2 + 1 >= k:
        print(1 + 2 * (k - 1))
    else:
        print(2 + 2 * (k - (n // 2 + 1) - 1))
