# https://programmers.co.kr/learn/courses/30/lessons/42883


def solution(number, k):
    greed = []
    for num in number:
        # 가장큰수를 만들기위해선 앞자리수를 최대한 크게 만들어야하므로 while문으로 가장 큰수를 앞에 놓음
        while greed and greed[-1] < num and k > 0:
            greed.pop()
            k -= 1
        greed.append(num)
        print(greed)
    return "".join(greed[: len(greed) - k])  # 마지막에 남아있을수있는 k고려
