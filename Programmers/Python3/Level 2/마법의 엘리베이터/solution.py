# https://school.programmers.co.kr/learn/courses/30/lessons/148653


def solution(storey):
    count = 0

    while storey > 0:
        cur_floor = storey % 10
        # 0 ~ 4는 내림, 6 ~ 9는 올리는게 가장 빠름
        if cur_floor > 5:
            count += 10 - cur_floor
            storey += 10
        elif cur_floor < 5:
            count += cur_floor
        else:
            # 기준을 4로 정한이유는 십의자리숫자가 4일때 일의자리에서 올림을해서 5가된경우 5는 내림, 올림 둘다 5번이기때문에 상관이없지만
            # 십의자리가 5 ~ 9인경우 일의자리에서 올림을 했을때 6 ~ 10이 되는데 이경우는 올림이 가장 빠르기때문
            next_floor = storey // 10 % 10
            if next_floor > 4:
                storey += 10
            count += cur_floor

        storey //= 10
    return count
