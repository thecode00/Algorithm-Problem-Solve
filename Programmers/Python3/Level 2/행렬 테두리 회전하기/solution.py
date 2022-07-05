# https://programmers.co.kr/learn/courses/30/lessons/77485
# 행렬을 직접 구현해서 메모리부족을 걱정했는데 rows, columns의 최대크기가 100이라
# int(4byte) * 100 * 100 = 40mb라서 메모리부족이 뜨지않았다

def solution(rows, columns, queries):
    answer = []
    matrix = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            matrix[i].append((i) * columns + (j + 1))
    for y1, x1, y2, x2 in queries:
        # 행렬회전이 끝난후 왼쪽위에있는수는 그냥 사라져버리므로 저장해둔다음 회전이끝난후 따로 처리
        temp = matrix[y1 - 1][x1 - 1]
        min_value = temp    # 가장작은값을 저장할 변수 임시로 왼쪽위의 값으로 초기화
        # 사라지는 수를 1개로 만들기위해 왼쪽세로, 아래가로, 오른쪽세로, 위세로 순서대로 회전시켜야한다
        for y in range(y1 - 1, y2 - 1):
            min_value = min(min_value, matrix[y + 1][x1 - 1])
            matrix[y][x1 - 1] = matrix[y + 1][x1 - 1]
        for x in range(x1 - 1, x2 - 1):
            min_value = min(min_value, matrix[y2 - 1][x + 1])
            matrix[y2 - 1][x] = matrix[y2 - 1][x + 1]
        for y in range(y2 - 1, y1 - 1, -1):
            min_value = min(min_value, matrix[y - 1][x2 - 1])
            matrix[y][x2 - 1] = matrix[y - 1][x2 - 1]
        for x in range(x2 - 1, x1 - 1, -1):
            min_value = min(min_value, matrix[y1 - 1][x - 1])
            matrix[y1 - 1][x] = matrix[y1 - 1][x - 1]
        matrix[y1 - 1][x1] = temp   # 사라진번호 처리
        answer.append(min_value)
    # print(matrix)
    return answer
