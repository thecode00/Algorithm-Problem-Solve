# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    # 숫자의 자릿수로 정렬을 하기위해 원소들을 문자로 바꿈
    numbers = list(map(str, numbers))
    # 원소의 최대값이 1000이기때문에 자릿수를 맞춰주기 위해 x * 4으로 key를 줌
    numbers.sort(key=lambda x: x * 4, reverse=True)
    answer = str(int("".join(numbers)))  # 0이 들어왔을때 0이 중복되는것을 막기 위해 int로 변환
    return answer
