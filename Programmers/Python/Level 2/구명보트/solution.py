# https://school.programmers.co.kr/learn/courses/30/lessons/42885

# deque를 이용해서 풀려고했지만 empty리스트에서 pop을 하는 경우가 생겼기에 인덱스로 품
def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) - 1
    # 최대값과 최소값을 비교해서 계속 최대값을 지워나가는 식
    while start <= end:
        if people[start] + people[end] > limit:
            answer += 1
        else:
            answer += 1
            start += 1
        end -= 1
    return answer
