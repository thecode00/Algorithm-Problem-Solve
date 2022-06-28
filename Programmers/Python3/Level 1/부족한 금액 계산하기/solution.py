# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):

    total = count * (2 * price + (count - 1) * price) // 2  # 수열의 함 공식 사용
    answer = money - total
    if answer > 0:  # 금액이 부족하지 않으면 0반환
        answer = 0
    else:
        answer = abs(answer)
    return answer
