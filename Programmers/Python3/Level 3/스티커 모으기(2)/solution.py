# https://school.programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    if len(sticker) <= 2:
        return max(sticker)
    # dp1은 첫번째 스티커를 쓴경우, dp2는 첫번째 스티커를 쓰지않은경우
    dp1, dp2 = [0] * len(sticker),  [0] * len(sticker)
    dp1[0] = dp1[1] = sticker[0]
    for idx in range(2, len(sticker) - 1):
        # 현재 스티커를 붙일때와 붙이지않을경우를 비교
        dp1[idx] = max(sticker[idx] + dp1[idx - 2], dp1[idx - 1])

    for idx in range(1, len(sticker)):
        # 현재 스티커를 붙일때와 붙이지않을경우를 비교
        dp2[idx] = max(sticker[idx] + dp2[idx - 2], dp2[idx - 1])
    return max(dp1[-2], dp2[-1])
