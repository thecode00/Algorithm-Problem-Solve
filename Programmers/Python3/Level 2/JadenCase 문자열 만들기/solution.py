# https://school.programmers.co.kr/learn/courses/30/lessons/12951


from curses.ascii import isalnum


def solution(s):
    answer = ''
    case_flag = True    # 현재 인덱스가 단어의 맨 앞부분인지 확인하는 플래그
    for idx in range(len(s)):
        if isalnum(s[idx]):
            if case_flag:
                answer += s[idx].upper()
                case_flag = False
            else:
                answer += s[idx].lower()
        elif s[idx] == " ":
            case_flag = True    # 공백이나오면 다음단어의 맨 앞부분을 위해 플래그를 True로 설정
            answer += " "
    return answer
