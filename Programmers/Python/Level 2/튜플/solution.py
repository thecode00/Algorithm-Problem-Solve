# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    s = s[2: -2]    # {{, }} 제거
    s = s.split("},{")
    s.sort(key=len)   # 길이 순으로 정렬
    for i in s:
        i_split = i.split(",")  # 쉼표로 나누면 숫자들만 남음
        for num in i_split:
            if int(num) not in answer:
                answer.append(int(num))
    return answer
