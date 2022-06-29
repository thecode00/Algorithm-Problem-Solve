# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ""
    while n > 0:
        n, re = divmod(n, 3)    # divmod함수는 몫과 나머지를 반환해줌
        answer += str(re)
    return int(answer, 3)   # int함수는 base진법으로 만들어진 문자열을 10진법으로 바꿔줌
