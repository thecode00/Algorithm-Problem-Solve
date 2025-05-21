# https://codeforces.com/problemset/problem/978/B

n = int(input())
file_name = input()

idx = 0
delete_count = 0

while idx < n:
    if file_name[idx] == "x":
        count = 0

        while idx < n and file_name[idx] == "x":
            count += 1
            idx += 1

        if count >= 3:
            delete_count += count - 2
        continue

    idx += 1
print(delete_count)
