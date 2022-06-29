# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = [[] * n]
    for y in range(n):
        for x in range(n):
            if arr1[y][x] == "#" or arr2[y][x] == "#":  # map1과 map2중 하나라도 벽이있다면 실제지도에도 벽이있음
                answer[y].append("#")
            else:
                answer[y].append(" ")
    print(answer)
    return answer
