# https://programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []
    for num in range(left, right + 1):
        # 1차원 배열로 놨을때 각 위치는 인덱스를 n으로 나눈 (몫, 나머지)
        answer.append(max(divmod(num, n)) + 1)
    return answer
