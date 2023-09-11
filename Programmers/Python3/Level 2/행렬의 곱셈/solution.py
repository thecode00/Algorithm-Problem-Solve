# https://school.programmers.co.kr/learn/courses/30/lessons/12949


def solution(arr1, arr2):
    # arr1이 n * m이고 arr2가 m * k일경우 행렬곱의 결과의 크기는 n * k
    matrix = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    print(matrix)

    for n in range(len(arr1)):
        for k in range(len(arr2[0])):
            for m in range(len(arr2)):
                matrix[n][k] += arr1[n][m] * arr2[m][k]
    return matrix
