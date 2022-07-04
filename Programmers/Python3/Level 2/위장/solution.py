# https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter


def solution(clothes):
    answer = 1
    # 옷의 착용위치별로 옷의 개수가 몇개인지 셈
    count = Counter([position for name, position in clothes])
    # 옷을 1개부터 가지고있는 옷의 종류개수까지 입을수있으므로 len(count)까지 for반복을한다
    for num in count.values():
        answer *= num + 1   # 옷의 종류를 입지않은경우가 있으므로 +1을 한다
    print(count)
    return answer - 1   # 옷을 아무것도 입지 않은 조합을 뺌
