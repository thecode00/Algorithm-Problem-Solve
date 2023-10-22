# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow  # 총 카펫수
    min_length = (total // 3)   # 갈색카펫이 노란색카펫을 감싸야하므로 최소길이는 3이된다
    # 가로길이는 세로길이보다 크거나 같아야하므로 세로길이를 최소길이부터 시작하여 탐색
    for h in range(3, min_length + 1):
        if total % h == 0:
            w = total // h
            # 둘레의 카펫수는 가로길이 * 2 + 세로길이 * 2에서 중복된카펫 4개를 빼준다
            if 2 * (h + w - 2) == brown:
                return [w, h]
    return answer
