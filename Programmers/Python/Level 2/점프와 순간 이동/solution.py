# https://school.programmers.co.kr/learn/courses/30/lessons/12980


def solution(n):
    count = 0
    while n > 0:
        q, r = divmod(n, 2)  # q = 몫, r = 나머지
        if r:   # 홀수일때만 한칸뒤로 이동하면서 배터리 사용
            count += 1
        n = q
    return count


print(solution(5000))
