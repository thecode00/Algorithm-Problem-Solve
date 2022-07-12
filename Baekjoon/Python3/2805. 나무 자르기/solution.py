# https://www.acmicpc.net/problem/2805

# pypy3 제출
n, m = map(int, input().split())    # 나무의 개수, 필요한 나무길이
trees = list(map(int, input().split()))

start, end = 1, max(trees)
while start <= end:
    mid = (start + end) >> 1    # 비트연산으로 2를 나눔
    total = 0   # 절단해서 얻은 총 나무길이
    for tree in trees:
        if tree <= mid:  # 나무의 길이가 절단기보다 작을때는 넘어감
            continue
        total += tree - mid
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
