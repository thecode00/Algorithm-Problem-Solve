# https://school.programmers.co.kr/learn/courses/30/lessons/17678


from collections import deque


def solution(n, t, m, timetable):
    timetable = [int(t[:2]) * 60 + int(t[3:])
                 for t in timetable]   # 시간을 모두 분단위로 변환
    timetable.sort()
    timetable = deque(timetable)

    cur_time = 540  # 09:00시

    for _ in range(n):
        for _ in range(m):
            # 대기열이 있다면 맨 마지막 사람의 1분전에 와야함
            if timetable and timetable[0] <= cur_time:
                answer = timetable.popleft() - 1
            else:   # 대기가 없거나 늦게타도 자리가있는경우 정시에 탑승
                answer = cur_time
        cur_time += t

    h, m = divmod(answer, 60)

    return str(h).zfill(2) + ":" + str(m).zfill(2)
