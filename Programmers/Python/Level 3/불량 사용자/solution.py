# https://school.programmers.co.kr/learn/courses/30/lessons/64064

from collections import defaultdict
import re


def solution(user_id, banned_id):
    ban_match_id = defaultdict(set)
    # 정규표현식을 사용해서 banned_id에 매칭되는 id를 찾음
    for idx, id in enumerate(banned_id):
        # "*"문자를 모든 문자가 매칭되는 "."으로 바꿔줌
        banned_id[idx] = id = id.replace("*", ".")
        p = re.compile(id)

        for i in user_id:
            m = re.match(p, i)
            # print(m)
            if m and len(i) == len(id):
                ban_match_id[id].add(m.group())
    print(ban_match_id)

    def dfs(i):
        if i >= len(banned_id):
            # 테스트케이스 #2에서 중복된 id조합을 없애기위해 list로 변환한다음 정렬을하고 set에 넣어서 중북을 방지하기위해 tuple로 변환함
            print(used)
            combinations_id.add(tuple(sorted(list(used))))
            return
        for t in ban_match_id[banned_id[i]]:
            if t not in used:
                used.add(t)
                dfs(i + 1)
                used.remove(t)

    combinations_id = set()
    used = set()    # 중복 id를 피하기위해 set사용
    dfs(0)
    # print(combinations_id)
    return len(combinations_id)


# 테스트케이스 #2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
