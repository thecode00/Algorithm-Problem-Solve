# https://codeforces.com/problemset/problem/122/A

num = int(input())


def is_lucky(num: int) -> bool:
    return all(n in "47" for n in str(num))


for i in range(1, 1001):
    if num % i == 0 and is_lucky(i):
        print("YES")
        break
else:
    print("NO")
