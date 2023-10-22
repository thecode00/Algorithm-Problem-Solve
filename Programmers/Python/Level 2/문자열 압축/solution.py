# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 + 1):
        compressed = ""  # 압축된 문자열
        prev = s[0:step]    # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # step 크기만큼 증가시키면서 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전상태와 동일하면 count증가
            if prev == s[j: j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j: j + step]   # 다시 상태 초기화
                count = 1
        compressed += str(count) + prev if count >= 2 else prev  # 이전 문자열 초기화
        answer = min(answer, len(compressed))
    return answer
