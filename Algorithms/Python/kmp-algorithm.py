from typing import List


s = "abcgesfjababaikpsobi"
find_str = "ababa"


def get_pi(s: str) -> List[int]:
    # Longest prefix suffix의 앞글자를 따서 lps라고 부르기도 함
    pi = [0] * len(s)
    longest = 0  # 가장 긴 prefix suffix의 길이
    # pi[0]은 항상 0이므로 1부터 탐색
    idx = 1
    while idx < len(s):
        # s[longest]는 prefix suffix의 다음 부분
        # Ex. s = "ababc" 일때 longest가 2라면 가장 긴 prefix suffix기 "ab"이고
        # "ab"의 다음인 s[longest] = s[2] = "a"를 가지고 비교
        if s[idx] == s[longest]:
            longest += 1
            pi[idx] = longest
            idx += 1
        else:
            if longest != 0:
                longest = pi[longest - 1]

            else:   # 일치하는 문자도 없고 긴 prefix suffix도 길이가 0이므로 pi[idx]를 0으로 설정
                pi[idx] = 0
                idx += 1

    return pi


def kmp(s: str, find_str: str):
    pi = get_pi(find_str)
    print(pi)

    i, j = 0, 0
    while i < len(s):
        if s[i] == find_str[j]:
            i += 1
            j += 1
        if j == len(find_str):
            return True
        if i < len(s) and s[i] != find_str[j]:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1
    return False


print(kmp(s, find_str))
print(kmp(s, "ababab"))
