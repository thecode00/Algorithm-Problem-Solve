# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# 문제대로 구현만 하면 되는문제, 중간에 break로 탐색을 멈출수도 있을거같은데 조건을 생각해봐야겠다
def solution(order):
    assitant = []
    count = 0
    for idx in range(1, len(order) + 1):
        assitant.append(idx)
        if assitant and assitant[-1] == order[count]:
            while assitant and assitant[-1] == order[count]:
                count += 1
                assitant.pop()

    return count
