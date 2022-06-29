# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):    # 3진수 구하는 문제와 비슷
    if n <= 3:
        return "124"[n - 1]
    else:
        q, r = divmod(n - 1, 3)  # 3진법에는 0이없기때문에 divmod(n - 1)을 함
        return solution(q) + "124"[r]


print(solution(7))
