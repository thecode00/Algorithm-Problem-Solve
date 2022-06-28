# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 3, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    for idx, ans in enumerate(answers):  # enumerate함수는 인덱스와 리스트의 값을 튜플로 만들어줌
        # 패턴의 길이가 제각각이기 때문에 인덱스를 패턴의 길이로 나눠서 각패턴에 맞게 채점
        if pattern1[idx % len(pattern1)] == ans:
            score[0] += 1
        if pattern2[idx % len(pattern2)] == ans:
            score[1] += 1
        if pattern3[idx % len(pattern3)] == ans:
            score[2] += 1
    max_score = max(score)  # 최고 점수
    answer = []
    for idx in range(len(score)):
        if score[idx] == max_score:
            answer.append(idx + 1)
    return answer
