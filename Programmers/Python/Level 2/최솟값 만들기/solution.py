# https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A, B):
    answer = 0
    # A의 작은값과 B의 큰값순으로 곱해지도록 정렬
    A.sort()
    B = sorted(B, key=lambda x: -x)
    for a, b in zip(A, B):
        answer += a * b

    return answer
