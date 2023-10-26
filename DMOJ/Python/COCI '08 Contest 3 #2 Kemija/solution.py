# https://dmoj.ca/problem/coci08c3p2

import sys

input = sys.stdin.readline

vowels = {"a", "e", "i", "o", "u"}

word = input().strip()
result = ""
index = 0
while index < len(word):
    result += word[index]
    # Skip encoded string
    if word[index] in vowels:
        index += 2

    index += 1

print(result)
