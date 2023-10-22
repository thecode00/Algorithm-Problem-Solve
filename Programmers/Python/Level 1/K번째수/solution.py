# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp = array[i - 1: j]  # array리스트를 슬라이스한 임시 리스트
        temp.sort()
        answer.append(temp[k - 1])
    return answer
