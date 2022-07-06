# https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations


# permutation으로 완전탐색을 사용하여 품
def solution(k, dungeons):
    answer = 0
    length = len(dungeons)
    search = list(permutations([n for n in range(length)], length))
    for combi in search:
        temp_fatigue = k    # 이 조합의 피로도 변수
        temp_dungeon = 0    # 이 조합이 탐험가능한 던전 수
        for idx in range(length):
            # 현재 피로도가 최소피로도보다 낮을때는 넘어감
            if temp_fatigue < dungeons[combi[idx]][0]:
                continue
            else:
                temp_fatigue -= dungeons[combi[idx]][1]
                temp_dungeon += 1
        answer = max(answer, temp_dungeon)
    return answer
