# https://school.programmers.co.kr/learn/courses/30/lessons/42889


from bisect import bisect_left, bisect_right


def solution(N, stages):
    stages.sort()
    failure = []
    for i in range(1, N + 1):
        # 이진탐색으로 스테이지에 도달한 사람 수와 스테이지를 깬 사람수를 구함
        next, cur = bisect_right(stages, i), bisect_left(stages, i)
        stage_people = len(stages) - cur
        success_people = len(stages) - next
        if stage_people == 0:
            failure.append([0, i])
            continue
        failure.append([(stage_people - success_people) / stage_people, i])
    # 실패율 내림차순 정렬, 스테이지가 작은순으로 넣었으므로 안정정렬인 Timsort를 사용해서 실패율이 같다면 작은스테이지가 먼저 나오게 함
    failure.sort(key=lambda x: -x[0])
    return [stage for _, stage in failure]
