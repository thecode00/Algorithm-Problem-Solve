# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    str_list = list(s)  # 문자열은 문자를 바꾸는게 불가능하므로 리스트로 변환
    for idx in range(len(str_list)):
        # 초기에 알파벳의 인덱스를 찾기위해 A나 a의 아스키코드값만큼 뺀 값으로 인덱스를 찾음
        if str_list[idx].islower():    # 소문자인지 확인하는 함수
            str_list[idx] = chr(
                (ord(str_list[idx]) - ord("a") + n) % 26 + ord("a"))
        elif str_list[idx].isupper():   # 대문자인지 확인하는 함수
            str_list[idx] = chr(
                (ord(str_list[idx]) - ord("A") + n) % 26 + ord("A"))
    return "".join(str_list)
