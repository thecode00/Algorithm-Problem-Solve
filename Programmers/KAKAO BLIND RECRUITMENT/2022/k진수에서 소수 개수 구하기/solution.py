# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    base_converted_num = convert_base(n, k)

    prime = 0
    none_zero_nums = base_converted_num.split("0")
    for num in none_zero_nums:
        # split으로 생긴 빈 문자열과 소수의 가장 작은값은 2이므로 그보다 작은값들을 필터링
        if len(num) == 0 or int(num) < 2:
            continue
        num = int(num)
        # none_zero_nums의 최대값까지 소수를 구해서 num이 소수인지 판별하려했지만 메모리 문제로 인해 num마다 소수를 새로 판별
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                break
        else:   # 문제의 조건을 다 합치면 결국엔 소수판별 문제이므로 num이 소수일경우 prime증가
            prime += 1
    return prime


def convert_base(num, base):
    """
    num을 base지수로 변환하는 함수
    """
    convert = ""
    while num > 0:
        num, r = divmod(num, base)
        convert += str(r)
    return convert[::-1]


# TEST
print(solution(437674, 3))
