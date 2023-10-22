# https://www.acmicpc.net/problem/1302

from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
count = defaultdict(int)
# 책 판매수
for _ in range(n):
    count[input().rstrip()] += 1

maxCount = max(count.values())  # 가장 많이 팔린책의 판매수 찾기
maxKeys = []
# 가장 많이 팔린책 찾기
for key in count.keys():
    if count[key] == maxCount:
        maxKeys.append(key)
maxKeys.sort()  # 사전순으로 가장 작은것을 출력하시위해 정렬
print(maxKeys[0])
