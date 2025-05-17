# https://codeforces.com/problemset/problem/131/A

word = input()

is_all_upper = True

for idx in range(1, len(word)):
    if word[idx].islower():
        is_all_upper = False
        break

if is_all_upper:
    if word[0].islower():
        print(word[0].upper() + word[1:].lower())
    else:
        print(word.lower())
else:
    print(word)
