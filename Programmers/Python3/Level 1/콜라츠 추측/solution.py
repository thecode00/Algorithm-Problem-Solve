# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0  # 작업 수 카운트
    while answer <= 500:
        if num == 1:
            break
        num = num // 2 if num % 2 == 0 else num * 3 + 1
        answer += 1
    return answer if answer < 501 else -1   # 작업 횟수가 500번 이상이면 -1 반환
