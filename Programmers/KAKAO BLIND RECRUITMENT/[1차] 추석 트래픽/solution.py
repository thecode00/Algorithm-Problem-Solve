# https://school.programmers.co.kr/learn/courses/30/lessons/17676

def convert_time(time):
    # HH:MM:SS.SSS로 들어오는 시간 문자열을 초로 변환해주는 함수
    hour, minute, second = time.split(":")
    return int(hour) * 3600 + int(minute) * 60 + float(second)


def solution(lines):
    logs = []
    # 로그 시간을 초로 변환하고 이벤트가 시작되는 시간과 끝나는 시간을 구함
    for s in lines:
        _, minute, T = s.split()
        minute = convert_time(minute)
        T = float(T[:-1])
        logs.append([minute - T + 0.001, "s"])
        logs.append([minute, "e"])
    logs.sort(key=lambda x: x[0])

    answer = 1
    acc = 0  # 시작점에서 처리중인 이벤트 숫자
    for i, log1 in enumerate(logs):  # 각 이벤트가 시작되거나 끝나는 시점에서 1초내의 겹치는 이벤트 찾기
        cur_event = acc
        for log2 in logs[i:]:
            # 탐색 시작점에서 1초가 넘어간 이벤트가 나오면 탐색을멈춤
            # TODO: 부동소수점 문제때문에 .9999로 설정한것을 .999로 바꿀수있는지 방법 찾아보기
            if log2[0] - log1[0] > 0.9999:
                break
            # 새로운 이벤트가 시작되면 추가
            if log2[1] == "s":
                cur_event += 1
        answer = max(answer, cur_event)
        if log1[1] == "s":
            acc += 1
        else:
            acc -= 1

    return answer


# 테스트용
print(solution([
    "2016-09-15 01:00:04.002 2.0s",
    "2016-09-15 01:00:07.000 2s"
]))
