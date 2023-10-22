# https://www.acmicpc.net/problem/1008

# pypy3으로 제출해야 풀림
n = int(input())


def dfs(queen, xy_dif, xy_sum):  # 퀸 위치배열, 왼쪽, 오른쪽 대각 리스트
    p = len(queen)  # row의 인덱스
    count = 0
    if p == n:
        return 1
    for q in range(n):  # column의 인덱스
        # 같은 column에 없을때, 왼쪽대각, 오른쪽대각 판별
        if q not in queen and p - q not in xy_dif and p + q not in xy_sum:
            count += dfs(queen + [q], xy_dif + [p - q], xy_sum + [p + q])
    return count


print(dfs([], [], []))
