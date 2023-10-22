# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    convert, zero = 0, 0
    while s != "1":
        convert += 1
        one = 0
        for num in s:
            if num == "1":
                one += 1
            else:
                zero += 1
        s = str(bin(one)[2:])   # 앞에있는 0b를 제거하기위해 슬라이스 사용
    return [convert, zero]


print(solution("110010101001"))
