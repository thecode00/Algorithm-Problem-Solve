# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    original = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}    # 0 - 9까지의 set
    nums = original - set(numbers)  # set의 차집합 이용
    answer = 0
    for n in nums:  # 차집합에 남아있는수를 모두 더함
        answer += n
    return answer
