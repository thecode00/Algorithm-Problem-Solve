# https://school.programmers.co.kr/learn/courses/30/lessons/12936

def solution(n, k):
    answer = []
    # 팩토리얼을 미리 구해놓음
    factorial = [1, 1]
    for i in range(2, n):
        factorial.append(factorial[-1] * i)
    nums = list(range(1, n + 1))
    print(factorial)
    while n > 0:
        # 숫자 n개에서 첫번째 숫자 x가 가질수있는 조합수는 (n - 1)!
        q = k // factorial[n - 1]
        k %= factorial[n - 1]
        # n = 3, k = 4일때 처음에 q가 2가되고 k가 0이되는데 답은 q가 두번째 순서인 1이다.
        # 이건 나머지가 0일때마다 다음순서로 넘어가서 생기는일이라서 나머지가 0일때를 따로 처리
        if k == 0:
            answer.append(nums.pop(q - 1))
        else:
            answer.append(nums.pop(q))
        n -= 1
    return answer


print(solution(3, 5))
