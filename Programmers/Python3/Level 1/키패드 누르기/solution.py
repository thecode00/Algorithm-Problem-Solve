# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    num_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (
        1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    # 시작 위치 좌표
    left = "*"
    right = "#"
    answer = ''

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            curPos = num_dict[num]
            # 오른손의 위치와 왼손의 위치가 현재 숫자의 좌표와 얼마나 떨어져 있는지 절대값으로 구함
            right_point = abs(curPos[0] - num_dict[right][0]) + \
                abs(curPos[1] - num_dict[right][1])
            left_point = abs(curPos[0] - num_dict[left][0]) + \
                abs(curPos[1] - num_dict[left][1])
            if right_point > left_point:    # 오른손이 왼손보다 멀리 있는경우
                answer += "L"
                left = num
            elif right_point < left_point:  # 오른손이 왼손보다 가까이 있는경우
                answer += "R"
                right = num
            else:   # 양손이 같은 거리에 있는경우 주로 사용하는 손을 씀
                if hand == "right":
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num
    return answer
