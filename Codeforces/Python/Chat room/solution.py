# https://codeforces.com/problemset/problem/58/A

chat = input()
hello = "hello"
index = 0
answer = ""
for s in chat:
    if s == hello[index]:
        answer += s
        index += 1
    if index == 5:
        print("YES")
        break
else:   # When for loop does not execute break else will be execute
    print("NO")
