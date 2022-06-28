# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    strings = list(s.split(" "))   # 문자열을 공백으로 리스트
    for index in range(len(strings)):
        temp_string = strings[index].lower()   # 문자열을 모두 소문자로 만듬
        temp_list = list(temp_string)   # 임시 문자열을 리스트로 저장
        for idx in range(len(temp_string)):
            if idx % 2 == 0:    # 파이썬 인덱스는 짝수지만 실제문자열 인덱스는 홀수임
                temp_list[idx] = temp_string[idx].upper()
        strings[index] = "".join(temp_list)  # 임시 문자열 리스트에 처리된 문자열을 문자리스트에 저장

    return " ".join(strings)
