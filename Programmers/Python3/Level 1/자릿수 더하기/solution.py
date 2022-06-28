# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    for num in list(str(n)):    # 숫자값을 문자 리스트로 만들어 분리
        answer += int(num)
    return answer
