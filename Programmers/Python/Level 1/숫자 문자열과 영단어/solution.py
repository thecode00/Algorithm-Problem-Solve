# https://programmers.co.kr/learn/courses/30/lessons/81301

# 처음에 시도했던 코드 처음에 아무생각도 안나서 그냥 때려넣은 코드
# def solution(s):    # 무지성 코드
#     s = s.replace("one", "1").replace("two", "2").replace(
#         "three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0")
#     answer = int(s)
#     return answer

def solution(s):
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    # 변환할 값들을 딕셔너리에 넣고 반복문으로 처리함
    for key in num_dict.keys():
        s = s.replace(key, num_dict[key])
    answer = int(s)
    return answer
