# https://school.programmers.co.kr/learn/courses/30/lessons/92341


from collections import defaultdict
from math import ceil


def solution(fees, records):
    total_parking_time = defaultdict(int)
    enter_car = {}
    for record in records:
        info = record.split()
        if info[2] == "IN":
            enter_car[info[1]] = convert_to_minute(info[0])
        else:
            parking_time = convert_to_minute(info[0]) - enter_car[info[1]]
            total_parking_time[info[1]] += parking_time
            del enter_car[info[1]]
    # 출차 기록이 없는 차들의 주차시간 계산
    end_time = convert_to_minute("23:59")
    for key, item in enter_car.items():
        total_parking_time[key] += end_time - item

    total = []
    # 번호가 작은 순부터 꺼내기위해 key리스트를 정렬
    for key in sorted(total_parking_time.keys()):
        total_fee = fees[1]  # 요금의 최소값은 기본 요금
        if total_parking_time[key] > fees[0]:
            total_fee += ceil((total_parking_time[key] - fees[0]) / fees[2]) * fees[3]
        total.append(total_fee)
    return total


def convert_to_minute(time):
    return int(time[:2]) * 60 + int(time[3:])


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
