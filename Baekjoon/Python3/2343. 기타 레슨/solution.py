# https://www.acmicpc.net/problem/2343

n, m = map(int, input().split())    # 강의 개수, 블루레이 개수
courses = list(map(int, input().split()))
start, end = max(courses), sum(courses)
while start <= end:
    mid = (start + end) >> 1    # 비트 연산으로 2로 나눔
    amount_video = 1    # 블루레이의 시간이 mid일때 나오는 블루레이의 수
    time_video = 0  # 현재 비디오의 총 시간
    for idx in range(n):
        if time_video + courses[idx] > mid:
            amount_video += 1
            time_video = courses[idx]
        else:
            time_video += courses[idx]
    if amount_video > m:    # start는 amount_video가 m인 마지막 값이 됌
        start = mid + 1
    else:
        end = mid - 1
print(start)
