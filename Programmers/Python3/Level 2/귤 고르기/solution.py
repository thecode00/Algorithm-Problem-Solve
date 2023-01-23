# https://school.programmers.co.kr/learn/courses/30/lessons/138476


from collections import Counter


def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine).most_common()
    print(count)
    while k > 0:
        k -= count[answer][1]
        answer += 1
        
    return answer