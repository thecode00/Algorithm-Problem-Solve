# https://school.programmers.co.kr/learn/courses/30/lessons/12979

from math import ceil


def solution(n, stations, w):
    count, start = 0, 1
    # 안테나의 범위 = 왼쪽범위(w) + 설치지점(1) + 오른쪽범위(w)
    antenna_range = 2 * w + 1
    # 기본 아이디어: 처음 설치되어있는 안테나를 기준으로 왼쪽, 오른쪽 구간이 나뉘어지는데
    # 이때 안테나의 왼쪽부분에 전파가 닿지않는 부분에 안테나의 범위를 최대한으로 이용
    for station in stations:
        if station - w > start:  # 안테나의 왼쪽에 전파가 닿지않는 부분이 있을때만 설치
            count += ceil((station - w - start) / antenna_range)
        start = station + w + 1

    if start <= n:  # 마지막 안테나의 오른쪽에 전파가 닿지않는 범위가 있다면 안테나 설치
        count += ceil((n - start + 1) / antenna_range)

    return count
