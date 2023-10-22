# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    length = len(prices)
    answer = [n for n in range(length - 1, -1, -1)]    # 각 인덱스의 시간을 max값으로 초기화
    for idx in range(length):
        for i in range(idx, length):
            if prices[idx] > prices[i]:  # 주식가격이 떨어졌을때만 시간을 다시 설정
                answer[idx] = i - idx
                break
    return answer

# 내가 푼 방식보다 시간효율이 더 좋은 알고리즘
# https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9-Python


def solution(prices):
    length = len(prices)
    answer = [i for i in range(length - 1, -1, -1)]  # 각 인덱스의 시간을 max값으로 초기화
    stack = [0]
    # 스택에 아직 가격이 떨어지지않은 주식들의 인덱스를 저장해놓고 주식이 떨어졌을때 스택안에있는 주식들과 비교해서 다시 시간을 초기화함
    for i in range(1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
