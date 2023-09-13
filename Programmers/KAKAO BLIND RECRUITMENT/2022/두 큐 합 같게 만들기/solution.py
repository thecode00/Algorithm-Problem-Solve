# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    total1, total2 = sum(queue1), sum(queue2)
    # queue1에서 queue2로 모든원소를 보낸후 다시 원래모습대로 만들기위해 필요한 연산수 len(queue1) * 4
    # Ref: https://a-littlecoding.tistory.com/123
    for count in range(len(queue1) * 4):
        if total1 == total2:
            return count
        elif total1 > total2:
            total1, total2 = move_num(queue1, queue2, total1, total2)
        else:
            total2, total1 = move_num(queue2, queue1, total2, total1)
    return -1


def move_num(give, get, give_total, get_total):
    """
    Args:
        give: 숫자를 넘겨줄 queue
        get: give로부터 숫자를 받을 queue

    Return:
        num을 넘겨준 후의 give와 get의 총합을 반환
        """
    num = give.popleft()
    get.append(num)
    return give_total - num, get_total + num


solution([1, 1], [1, 5])
