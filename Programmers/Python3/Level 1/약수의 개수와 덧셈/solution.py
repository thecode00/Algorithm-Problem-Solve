# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        count = 0   # 해당숫자의 약수의 개수
        for i in range(1, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                count += 1
                # 약수는 항상 짝이되는수가 있기때문에 추가
                if i ** 2 != num:   # 제곱수일땐 짝이되는수가 자기자신이기 때문에 제외
                    count += 1
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer
