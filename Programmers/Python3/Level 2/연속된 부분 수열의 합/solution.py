# https://school.programmers.co.kr/learn/courses/30/lessons/178870


def solution(sequence, k):
    # 투 포인터 방식
    answer = []
    total = 0   # left ~ right까지의 합
    left = 0
    for right in range(len(sequence)):
        total += sequence[right]
        # sequence에 음수가 없기때문에 left ~ right까지의 합이 k보다 크다면 그 다음 원소를 더해도 k를 만들수 없다
        # 그래서 left를 total이 k보다 작거나 같은값이 될때까지 움직임
        while left < right and total > k:
            total -= sequence[left]
            left += 1
        if total == k:
            answer.append([left, right])
    # 합이 k인 부분수열을 길이, 시작인덱스가 작은순으로 정렬
    answer.sort(key=lambda x: (x[1] - x[0], x[0]))
    return answer[0]
