# https://codeforces.com/problemset/problem/122/A

num = input()
if num.count("4") + num.count("7") == len(num):
    print("YES")
else:
    for i in range(1, int(num) // 2 + 1):
        if str(i).count("4") + str(i).count("7") == len(str(i)):
            if int(num) % i == 0:
                print("YES")
                break
    else:
        print("NO")