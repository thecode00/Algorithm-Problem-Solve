# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if prime[num]:
            j = 2
            answer += 1
            while num * j <= n:
                prime[num * j] = False
                j += 1

    return answer
