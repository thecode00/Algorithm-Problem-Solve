# https://www.acmicpc.net/problem/2512

n = int(input())
budgets = list(map(int, input().split()))   # 예산리스트
max_budget = int(input())

start, end = 1, max(budgets)
while start <= end:
    mid = (start + end) >> 1    # 비트연산으로 2로 나눔
    total = max_budget
    for num in budgets:
        if mid > num:
            total -= num
        else:
            total -= mid
    if total < 0:   # 예산이 부족할때
        end = mid - 1
    else:   # 예산이 충분할때
        start = mid + 1
print(end)
