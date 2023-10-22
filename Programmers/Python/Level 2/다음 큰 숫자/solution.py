# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    n_bits = bits_count(n)    # n의 1비트개수를 저장
    while True:
        n += 1
        cur_bits = bits_count(n)
        if n_bits == cur_bits:
            return n


def bits_count(num):
    total = 0
    while num:
        """
        1은 0001의 비트를 가지고있으므로 1과 AND연산을하면 현재 숫자의 최하위비트(LSB) 즉 맨 오른쪽비트가 1인지 0인지 알수있음
        """
        total += num & 1
        num >>= 1
    return total


print(solution(5))
