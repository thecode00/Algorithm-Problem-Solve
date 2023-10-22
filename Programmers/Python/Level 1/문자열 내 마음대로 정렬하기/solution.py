# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = list(strings)
    # 같은 문자열이 존재할경우 사전순정렬을 해야하므로 람다에 x추가
    answer.sort(key=lambda x: (x[n], x))
    return answer
