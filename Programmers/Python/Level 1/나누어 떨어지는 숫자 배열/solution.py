# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if answer:  # answer가 비어있지 않을때
        return sorted(answer)
    return [-1]
