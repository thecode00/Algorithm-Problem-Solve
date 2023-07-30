# https://school.programmers.co.kr/learn/courses/30/lessons/17686

from curses.ascii import isdigit


def solution(files):
    # 정렬을위해 파일이름 분리
    for idx, file in enumerate(files):
        cur = file.lower()
        # HEAD와 NUMBER의 인덱스찾기
        head_idx = 0
        while head_idx < len(file):
            if isdigit(cur[head_idx]):
                break
            head_idx += 1

        num_idx = head_idx
        while num_idx < len(file):
            if not isdigit(cur[num_idx]):
                break
            num_idx += 1

        files[idx] = [cur[:head_idx], int(cur[head_idx: num_idx]), cur[num_idx:], file]
    # 이름순, NUMBER오름차순 정렬, 파이썬의 정렬은 Timsort를 사용하고 안정정렬이라 순서가 유지됨
    files.sort(key=lambda x: (x[0], x[1]))

    answer = [file for _, _, _, file in files]
    return answer
