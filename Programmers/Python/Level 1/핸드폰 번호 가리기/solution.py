# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    length = len(phone_number) - 4  # 별의 개수
    answer = '*' * length + phone_number[-4:]   # 끝에서 4번째부터 끝부분까지 슬라이스
    return answer
