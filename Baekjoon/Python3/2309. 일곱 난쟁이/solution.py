# https://www.acmicpc.net/problem/2309

from itertools import combinations
import sys

input = sys.stdin.readline

# 라이브러리 사용코드
dwarfs = [int(input()) for _ in range(9)]

for comb in combinations(dwarfs, 7):
    if sum(comb) == 100:
        for dwarf in sorted(comb):
            print(dwarf)
        break

# 라이브러리 사용하지 않은 코드
# 아이디어: 9명의 난쟁이들중 뺄 2명의 난쟁이들을 선택
dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
height = sum(dwarfs)


def solve():
    for i in range(8):
        for j in range(i + 1, 9):
            if height - dwarfs[i] - dwarfs[j] == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(dwarfs[k])
                return


solve()
