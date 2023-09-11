# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):  # 처음 코드
    answer = []
    for num in numbers:
        # 짝수는 LSB가 항상 0이므로 1을 더해주면 됨
        if num % 2 == 0:
            answer.append(num + 1)
        # 홀수는 LSB가 1이라 1을 더할경우 상위비트들이 다 변할수가 있어서 가장 낮은위치에 있는 0비트를 1로 바꿔주고 x보다 크지만 차이가 가장 적은 수로 만들기위해
        # 0비트의 오른쪽에 있는 1비트를 0으로 바꿔줌
        # Ex. 15(1111) + 1(0001) = 16(10000), 15(1111)의 경우 가장 낮은위치에 있는 0비트는 01111이므로 0비트를 1로 바꿔주고 0비트의 오른쪽에 있던 1비트를 0으로 바꿔줌 => 23(10111)
        else:
            # 비트가 다 1로 차있는 비트일때를 대비해서 0을 찾기위해 첫번째위치에 0을 추가
            bin_num = ["0"] + list(bin(num)[2:])
            for idx in range(len(bin_num) - 1, -1, -1):
                if bin_num[idx] == "0":
                    bin_num[idx] = "1"
                    bin_num[idx + 1] = "0"
                    break
            answer.append(int("".join(bin_num), 2))
    return answer


def solution(numbers):  # 두번째 코드, 홀수에서 0비트를 찾는부분을 개선
    answer = []
    for num in numbers:
        # 짝수는 LSB가 항상 0이므로 1을 더해주면 됨
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            compare_bit = 1
            while True:
                if not (compare_bit & num):
                    break
                # 1비트의 위치를 왼쪽으로 한칸씩 옮김
                compare_bit *= 2
            # 가장 낮은위치에있는 0비트의 위치를 찾은후 그 비트의 오른쪽에있는 1비트의 위치로 옮긴다음 더하면 그 1비트는 0이되고 0비트는 1이됨
            # Ex. 11(1011) + 2(0010) = 13(1101)
            compare_bit >>= 1
            answer.append(compare_bit + num)

    return answer


def solution(numbers):  # 프로그래머스에 답변으로 있던코드, Ref: https://school.programmers.co.kr/learn/courses/30/lessons/77885/solution_groups?language=python3
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) + val + 1)

    return answer
