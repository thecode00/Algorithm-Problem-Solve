# https://programmers.co.kr/learn/courses/30/lessons/60058

# 균형잡힌 문자열의 인덱스를 반환하는 함수
def check_balance(string):
    count = 0
    for idx in range(len(string)):
        if string[idx] == "(":
            count += 1
        elif string[idx] == ")":
            count -= 1
        if count == 0:  # 균형잡혔을때
            return idx

# 올바른 문자열인지 확인하는 함수


def check_correct(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        else:
            if count == 0:  # 짝이 맞지않을때
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return p
    index = check_balance(p)
    u, v = p[: index + 1], p[index + 1:]    # 문자열을 u, v로 나눔
    if check_correct(u):
        answer = u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        u = list(u[1: -1])
        for par in u:
            if par == "(":
                answer += ")"
            else:
                answer += "("
    return answer
