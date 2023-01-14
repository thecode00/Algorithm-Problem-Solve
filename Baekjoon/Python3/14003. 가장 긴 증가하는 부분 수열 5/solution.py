# https://www.acmicpc.net/problem/14003


from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
length = [1 for _ in range(n)]  # 최대LIS길이를 저장할 리스트

lis = [sequence[0]]
# 0 ~ n번째 노드까지 최대LIS길이를 찾음
for idx in range(1, n):
    if lis[-1] < sequence[idx]:
        lis.append(sequence[idx])
        length[idx] = len(lis)
    else:
        index = bisect_left(lis, sequence[idx])
        length[idx] = index + 1
        lis[index] = sequence[idx]

max_length = max(length)    # 최대LIS길이
print(max_length)
max_index = length.index(max_length)    # 최대길이를 가지는 인덱스
answer = []
# 최대길이 인덱스부터 0까지 탐색하며 LIS를 구함
while max_length > 0:
    if length[max_index] == max_length:
        answer.append(sequence[max_index])
        max_length -= 1
    max_index -= 1

# answer리스트에 값이 큰 순서부터 들어갔기때문에 [::-1]슬라이스를 사용해서 작은값이 앞으로 오도록 설정
print(" ".join(map(str, answer[::-1])))
