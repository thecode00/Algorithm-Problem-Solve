# https: // codeforces.com/problemset/problem/1699/B

for _ in range(int(input())):
    n, m = map(int, input().split())
    pt1 = [1, 0]
    pt2 = [0, 1]
    save1 = []
    save2 = []
    p1 = ""  # It will be 1 0 0 1 ... pattern
    p2 = ""  # It will be 0 1 1 0 ... pattern
    for i in range(m // 2):
        if i % 2 == 0:
            save1 += pt1
            save2 += pt2
        else:
            save1 += pt2
            save2 += pt1
    p1 = " ".join(map(str, save1))
    p2 = " ".join(map(str, save2))
    print(p1)   # The pattern in the first line is fixed 1 0 0 1 0 0 1 ...
    for i in range((n - 2) // 2):
        if i % 2 == 0:
            print(p2)
            print(p2)
        else:
            print(p1)
            print(p1)
    if n % 4 == 0:
        print(p1)
    else:
        print(p2)
