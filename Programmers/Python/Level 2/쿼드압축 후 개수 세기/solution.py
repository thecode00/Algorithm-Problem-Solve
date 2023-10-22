# https://school.programmers.co.kr/learn/courses/30/lessons/68936

def solution(arr):
    answer = [0, 0]
    check_same(arr, 0, 0, len(arr), answer)
    return answer


def check_same(arr, start_x, start_y, size, answer):
    check_num = arr[start_y][start_x]
    for y in range(start_y, start_y + size):
        for x in range(start_x, start_x + size):
            if arr[y][x] != check_num:  # 다른 수가 나왔다면 4개로 나누고 재귀탐색
                new_size = size // 2
                check_same(arr, start_x, start_y, new_size, answer)
                check_same(arr, start_x + new_size, start_y, new_size, answer)
                check_same(arr, start_x, start_y + new_size, new_size, answer)
                check_same(arr, start_x + new_size, start_y + new_size, new_size, answer)
                return
    # 사각형의 모든 숫자가 같다면 해당 숫자의 개수 증가
    answer[check_num] += 1
