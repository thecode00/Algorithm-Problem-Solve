# https://programmers.co.kr/learn/courses/30/lessons/64061
# from collections import deque

# TODO:너무 복잡하게 푼 문제 수정필요
# def solution(board, moves):
#     length = len(board)
#     dolls = [deque([]) for _ in range(length)]   # 인형 위치 리스트
#     basket = []  # 인형 바구니
#     for x in range(length):  # 각 바닥마다 존재하는 인형을 가져올것이기 때문에 x루프내부에서 y루프를 돌림
#         for y in range(length):
#             if board[y][x] != 0:
#                 dolls[x].append(board[y][x])
#     answer = 0
#     for index in moves:
#         if len(dolls[index - 1]) > 0:   # 해당 바닥에 인형이 남아있을경우
#             # 인형을 위에서부터 체크했기때문에 선입선출구조로 해야한다
#             basket.append(dolls[index - 1].popleft())
#             basket, answer = check_pop(basket, answer)
#     return answer


# def check_pop(basket, answer):  # 바구니의 인형이 터지는지 확인하는 메소드
#     if len(basket) <= 1:
#         return basket, answer
#     if basket[-1] == basket[-2]:    # 바구니의 끝에서 2번째인형과 끝에있는 인형이 같다면 터트리고 반환
#         for _ in range(2):
#             basket.pop()
#             answer += 1
#     return basket, answer
