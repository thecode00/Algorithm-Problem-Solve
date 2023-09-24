# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return

        hanoi(n - 1, start, via, end)
        answer.append([start, end])
        hanoi(n - 1, via, end, start)
    hanoi(n, 1, 3, 2)
    return answer


solution(3)
