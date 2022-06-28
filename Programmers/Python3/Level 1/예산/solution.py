# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    d.sort()
    answer = 0
    for cost in d:
        if cost > budget:    # 더이상 지원이 불가한경우
            break
        answer += 1
        budget -= cost
    return answer
