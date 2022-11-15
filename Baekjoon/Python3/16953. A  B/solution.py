# https://www.acmicpc.net/problem/16953

import sys

input = sys.stdin.readline

a, b = map(int, input().split())


def dfs(num: int, target: int) -> int:
    if num < target:
        return -1
    elif num == target:
        return 1
    str_num = str(num)
    if str_num[-1] == "1":  # 맨 오른쪽숫자가 1일경우 1을 제거
        calc = dfs(int(str_num[: -1]), target)
    else:
        # num이 홀수라면 2로 나눌수가 없기때문에 -1 반환
        if int(str_num) % 2 != 0:
            return -1
        calc = dfs(int(str_num) // 2, target)
    return calc + 1 if calc != -1 else -1


print(dfs(b, a))
