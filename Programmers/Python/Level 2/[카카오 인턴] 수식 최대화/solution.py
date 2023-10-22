# https://school.programmers.co.kr/learn/courses/30/lessons/67257#

from itertools import permutations


def solution(expression):

    def split_calc(index, operators, expression):
        if index == 2:
            return str(eval(expression))

        # 현재 연산자를 기준으로 나눈다음 나눠진 식들을 연산자 우선순위대로 계산
        # Ex. operators = ["-", "+", "*"], ["50*6-3*2+6"] => ["50*6", "3*2+6"] => ["50*6", "3*2", "6"] => ["300", "6", "6"] => ["300", "12"] => ["288"]
        split_expression = expression.split(operators[index])
        for idx, e in enumerate(split_expression):
            split_expression[idx] = split_calc(index + 1, operators, e)

        return str(eval(f"{operators[index]}".join(split_expression)))
    # 연산자 순서의 순열을 구함, 맨 끝에있는 연산자가 가장 높은 우선순위를 가짐
    operators = permutations(["+", "-", "*"], 3)

    max_abs = 0
    for opers in operators:
        # 최대절대값을 구함, split_calc함수는 문자열을 반환하기때문에 정수로 변환해야함
        max_abs = max(max_abs, abs(int(split_calc(0, opers, expression))))

    return max_abs


print(solution("100-200*300-500+20"))
