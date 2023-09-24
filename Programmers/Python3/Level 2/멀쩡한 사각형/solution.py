# https://programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd


def solution(w, h):
    # 직접 그려보면 일정패턴이 w, h의 최대공약수만큼 반복되는걸 알수있다
    gcd_num = gcd(w, h)     # 잘리는 패턴의 반복 횟수
    pw, ph = w // gcd_num, h // gcd_num  # 패턴의 가로, 세로
    cut_area = ph + pw - 1
    return w * h - (cut_area * gcd_num)
