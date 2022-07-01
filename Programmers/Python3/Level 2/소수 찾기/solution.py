# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def solution(numbers):
    answer = 0
    nums = set()    # 중복값을 없애기 위해 set를 사용함
    for length in range(len(numbers)):
        # permutations을 이용하여 숫자들의 조합을 set에 저장
        per = list(permutations(numbers, length + 1))
        for num in per:
            nums.add(int("".join(num)))
    max_value = max(nums)
    prime = [True] * (max_value + 1)  # numbers의 조합중 최대값까지 소수를 판별
    for num in range(2, max_value + 1):  # 에라토스테네소의 체를 이용해 소수판별
        if prime[num]:
            for mul in range(num * 2, max_value + 1, num):
                prime[mul] = False
    for num in nums:
        if num < 2:  # 최소 소수는 2이므로 그 아래값은 무시
            continue
        if prime[num]:  # 소수일경우 +1
            print(num)
            answer += 1
    return answer
