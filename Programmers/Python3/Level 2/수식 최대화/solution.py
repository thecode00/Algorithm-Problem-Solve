# https://programmers.co.kr/learn/courses/30/lessons/67257
from itertools import permutations

# TODO: 나중에 풀기
# def solution(expression):
#     answer = 0
#     operator = list(permutations(["*", "+", "-"], 3))
#     print(expression.split(operator[0][0]))

#     for oper in operator:
#         temp = [expression]
#         for idx in range(0, 2):
#             for s in temp:
#                 temp = divide_string(s, oper[idx])
#             print(temp)
#     return answer
# # 문자열을 주어진 연산자로 나눠서 반환해주는 함수


# def divide_string(string, operator):
#     return list(string.split(operator))
