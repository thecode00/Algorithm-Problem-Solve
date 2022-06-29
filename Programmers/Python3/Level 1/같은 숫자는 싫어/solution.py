# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    answer.append(arr[0])   # 초기값
    for num in arr:
        # answer의 마지막값과 다르다면 중복된 숫자가 아니므로 추가
        if answer[-1] != num:
            answer.append(num)
    return answer
