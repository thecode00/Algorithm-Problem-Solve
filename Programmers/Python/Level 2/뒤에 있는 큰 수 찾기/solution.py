# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    answer = [-1] * len(numbers)
    # 아직 뒤에 큰수가 없는 숫자들의 인덱스
    stack = []
    for idx, num in enumerate(numbers):
        # 현재 인덱스의 숫자가 큰수가 될수있는 인덱스 찾기
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)

    return answer
