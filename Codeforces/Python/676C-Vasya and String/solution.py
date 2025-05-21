# https://codeforces.com/problemset/problem/676/C

def max_substring_length(s, k, target_char):
    max_len = 0
    left = 0
    count = 0

    for right in range(len(s)):
        if s[right] != target_char:
            count += 1

        while count > k:
            if s[left] != target_char:
                count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


n, k = map(int, input().split())
s = input()

result = max(max_substring_length(s, k, 'a'), max_substring_length(s, k, 'b'))
print(result)
