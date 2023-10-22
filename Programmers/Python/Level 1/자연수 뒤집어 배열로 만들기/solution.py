# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = list(str(n))
    answer.reverse()
    # 리스트를 만들때 문자열로 변환했으므로 map을 통해 int로 다시 바꿔줌
    return list(map(int, answer))
