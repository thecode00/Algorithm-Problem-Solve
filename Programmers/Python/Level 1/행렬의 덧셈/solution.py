# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for y in range(len(arr1)):
        for x in range(len(arr1[y])):
            answer[y].append(arr1[y][x] + arr2[y][x])
    return answer
