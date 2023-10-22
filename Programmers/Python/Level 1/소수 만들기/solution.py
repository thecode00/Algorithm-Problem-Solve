# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    answer = 0
    # 에라토스테네스의 체 사용
    # num의 최대숫자 개수가 50이고 최대 원소가 1000이므로 25000까지 체를 친다
    prime = [True for _ in range(50001)]
    for i in range(2, 25001):
        if prime[i]:    # prime[i]가 소수인경우 i배수를 다 False로 바꿈
            j = 2
            while i * j <= 50000:
                prime[i * j] = False
                j += 1
    for num in combinations(nums, 3):   # nums리스트에서 3개를 선택하는 조합
        if prime[sum(num)]:  # 3개의 숫자를 합친수가 prime리스트에서 True값일경우 소수이므로 answer += 1
            answer += 1

    return answer
