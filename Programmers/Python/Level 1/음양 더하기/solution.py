# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for pair in zip(absolutes, signs):  # zip함수로 두 리스트를 묶음
        if pair[1]:  # signs가 True일때
            answer += pair[0]
        else:   # signs가 False일때
            answer -= pair[0]
    return answer
