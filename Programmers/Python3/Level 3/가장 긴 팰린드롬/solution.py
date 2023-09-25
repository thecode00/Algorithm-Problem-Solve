# https://school.programmers.co.kr/learn/courses/30/lessons/12904#

def solution(s):
    answer = 0
    index = 0
    while index < len(s):
        end = index

        # 현재 문자열이 왼쪽끝인 같은문자열 펠린드롬을 찾음, 같은 문자열은 홀수든 짝수든 무조건 펠린드롬
        while end < len(s) and s[end] == s[index]:
            end += 1
        # 같은 문자열 펠린드롬의 양쪽에서 현재문자열 s[index]와 다른 문자열 펠린드롬 탐색
        start = index - 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        answer = max(answer, end - start - 1)
        index += 1
    return answer
