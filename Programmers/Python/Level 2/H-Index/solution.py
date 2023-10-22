# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    length = len(citations)
    for idx in range(length):
        # h-index값은 리스트안에 없어도 됨
        if length - idx <= citations[idx]:
            answer = length - idx
            break
    return answer
