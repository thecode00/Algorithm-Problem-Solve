# https://school.programmers.co.kr/learn/courses/30/lessons/17677


from collections import Counter
import re


def solution(str1, str2):
    l1, l2 = [], []
    # 정규식으로 알파벳만 골라냄
    for idx in range(len(str1) - 1):
        if re.match('[a-z]{2}', str1[idx:idx + 2].lower()):
            l1.append(str1[idx:idx + 2].lower())

    for idx in range(len(str2) - 1):
        if re.match('[a-z]{2}', str2[idx:idx + 2].lower()):
            l2.append(str2[idx:idx + 2].lower())

    c1, c2 = Counter(l1), Counter(l2)

    # and와 or 연산자로 합집합과 교집합을 구함
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())

    jaccard = 1 if union == 0 else intersection / union

    return int(jaccard * 65536)
