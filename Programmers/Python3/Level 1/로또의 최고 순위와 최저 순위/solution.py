# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    ranks = [1, 2, 3, 4, 5, 6, 6]
    zero = lottos.count(0)  # 0의 개수
    win = 6
    for num in range(len(lottos)):
        if lottos[num] in win_nums:
            win -= 1
    # 0의 갯수만큼 순위가 달라지므로 win - zero를 함
    answer = [ranks[win - zero], ranks[win]]
    return answer
