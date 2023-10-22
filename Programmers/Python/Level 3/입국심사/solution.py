# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    times.sort()
    start, end = 0, times[-1] * n   # 최대시간은 일처리가 가장 느린사람이 모든 사람을 다 커버하는경우
    while start < end:
        mid = start + (end - start) // 2
        passed = 0  # 각 심사관에게 mid분이 주어졌을때 입국심사대를 통과한 사람 수
        for t in times:
            passed += mid // t

        if passed >= n:
            end = mid
        else:
            start = mid + 1
    return end
