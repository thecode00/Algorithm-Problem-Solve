# https://school.programmers.co.kr/learn/courses/30/lessons/84512


"""
단어의 총개수가 5 ^ 1 + 5 ^ 2 + 5 ^ 3 + 5 ^ 4 + 5 ^ 5 = 3095개 이므로 브루트포스로 풀수있는 문제
"""


def solution(word):
    vowels = ["A", "E", "I", "O", "U"]

    def find(w, count):
        if w == word:
            return True, count
        if len(w) == 5:
            return False, count
        for idx in range(5):
            count += 1
            flag, count = find(w + vowels[idx], count)
            if flag:
                return True, count
        return False, count

    return find("", 0)[1]
