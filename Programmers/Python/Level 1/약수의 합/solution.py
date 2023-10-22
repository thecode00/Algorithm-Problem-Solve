# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    factor = []  # 약수들을 저장할 리스트
    for num in range(1, int(n ** .5) + 1):
        if n % num == 0:
            factor.append(num)
            if num ** 2 != n:   # 제곱수가 아닐때 약수와 짝이맞는 값을 추가
                factor.append(n // num)
    print(factor)
    answer = sum(factor)
    return answer
