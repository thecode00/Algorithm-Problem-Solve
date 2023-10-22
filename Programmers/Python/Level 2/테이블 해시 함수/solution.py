# https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    answer = 0
    # row가 0-index가 아니라 1-index로 주어지므로 주의
    for idx in range(row_begin, row_end + 1):
        total = 0
        for num in data[idx - 1]:
            total += num % idx
        # 튜플의 S_i XOR연산
        answer ^= total
    return answer
