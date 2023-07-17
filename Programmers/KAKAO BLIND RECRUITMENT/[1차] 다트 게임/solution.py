# https://programmers.co.kr/learn/courses/30/lessons/17682

# TODO: 나중에 풀기
def solution(dartResult):
    score = [0]
    for s in dartResult:
        if s == "S":
            score.append(0)
        elif s == "D":
            score[-1] **= 2
            score.append(0)
        elif s == "T":
            score[-1] **= 3
            score.append(0)
        elif s == "*":
            score[-1] *= 2
            if len(score) > 2:
                score[-2] *= 2
        elif s == "#":
            score[-1] *= -1
        else:
            score[-1] = score[-1] * 10 + int(s)
    return sum(score)


solution("1S2D*3T")
