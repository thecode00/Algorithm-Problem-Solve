# https://school.programmers.co.kr/learn/courses/30/lessons/135807

from math import gcd


def solution(arrayA, arrayB):
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    # 유클리드 호제법: x, y의 최대공약수는 y, z의 최대공약수와 같다
    for num_a, num_b in zip(arrayA, arrayB):
        gcd_a = gcd(gcd_a, num_a)
        gcd_b = gcd(gcd_b, num_b)

    print(gcd_a, gcd_b)
    # 다른쪽 카드를 나눌수있는지 확인
    can_divide_a = can_divide_b = False
    for num_a, num_b in zip(arrayA, arrayB):
        if num_a % gcd_b == 0:
            can_divide_a = True
        if num_b % gcd_a == 0:
            can_divide_b = True

    answer_a = answer_b = 0
    if not can_divide_a:
        answer_b = gcd_b
    if not can_divide_b:
        answer_a = gcd_a

    return max(0, answer_a, answer_b)
