# https://school.programmers.co.kr/learn/courses/30/lessons/155651


import heapq


def solution(book_time):    # heap 사용
    min_room = -float("inf")
    room = []

    for time in book_time:  # 분단위로 변환
        time[0] = int(time[0][:2]) * 60 + int(time[0][3:])
        time[1] = int(time[1][:2]) * 60 + int(time[1][3:]) + 10  # 청소시간 10분

    book_time.sort()    # 대실시간이 빠른순서대로 정렬
    for start, end in book_time:
        heapq.heappush(room, end)
        while room and room[0] <= start:
            heapq.heappop(room)
        min_room = max(min_room, len(room))

    return min_room


def solution(book_time):    # 배열만 사용
    min_room = -float("inf")
    room = []

    for time in book_time:  # 분단위로 변환
        time[0] = int(time[0][:2]) * 60 + int(time[0][3:])
        time[1] = int(time[1][:2]) * 60 + int(time[1][3:]) + 10  # 청소시간 10분

    book_time.sort()    # 대실시간이 빠른순서대로 정렬
    for start, end in book_time:
        room.append(end)
        room = sorted(room, key=lambda x: -x)
        while room and room[-1] <= start:   # 대실종료시각이 지난사람들 pop
            room.pop()
        min_room = max(min_room, len(room))

    return min_room
