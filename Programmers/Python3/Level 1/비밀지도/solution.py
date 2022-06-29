# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    # 2진수로 변환시켜 저장할 리스트
    bin_arr1 = []
    bin_arr2 = []
    answer = ["" for _ in range(n)]
    for index in range(n):
        # 2진수의 앞자리에도 n크기에 맞게 0이 생기게하기 위해 zfill함수를 사용
        bin_arr1.append(str(format(arr1[index], "b").zfill(n)))
        bin_arr2.append(str(format(arr2[index], "b").zfill(n)))
    for y in range(n):
        for x in range(n):
            # 1은 벽을나타냄, 둘중 하나라도 벽이있다면 실제지도에도 벽이있음
            if bin_arr1[y][x] == "1" or bin_arr2[y][x] == "1":
                answer[y] += "#"
            else:
                answer[y] += " "
    return answer
