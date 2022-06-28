# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 0
    for num in range(2, int(n / 2) + 1):    # 절반값이후는 최솟값인 2로 나누었을때를 넘어가므로 무시
        if (n - 1) % num == 0:
            answer = num
            break
    if answer == 0:  # 값을 찾지 못했을때는 답이 n - 1이 된다
        answer = n - 1
    return answer
