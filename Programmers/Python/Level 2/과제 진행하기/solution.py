# https://school.programmers.co.kr/learn/courses/30/lessons/176962#

def solution(plans):
    answer = []
    stack = []

    for plan in plans:
        hour, minute = map(int, list(plan[1].split(":")))

        start_time = hour * 60 + minute

        plan[1] = start_time
        plan[2] = int(plan[2])
    plans.sort(key=lambda x: (x[1]))

    remain_time = 0
    for plan in plans:
        # 하고있는숙제가 있는지 확인
        if stack and plan[1] - stack[-1][1] > 0:
            remain_time += plan[1] - stack[-1][1]

        # 남은시간동안 하고있던 숙제 다시하기
        while stack and remain_time:
            if stack[-1][2] <= remain_time:
                name, s_time, period = stack.pop()
                answer.append(name)
                remain_time -= period
            else:
                stack[-1][2] -= remain_time
                remain_time = 0

        remain_time = 0
        stack.append(plan)

    while stack:
        answer.append(stack.pop()[0])
    return answer
