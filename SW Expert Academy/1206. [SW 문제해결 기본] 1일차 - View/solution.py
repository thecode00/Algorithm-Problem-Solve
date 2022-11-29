"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&problemLevel=4&problemLevel=5&problemLevel=6&contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=6&pageSize=10&pageIndex=1
"""
pos = [-2, -1, 1, 2]

# n이 0 < n <= 1000 라서 5 * 1000 * 10 = 50000이 최대작업수라 완전탐색으로 품
for num in range(1, 11):
    n = int(input())
    buildings = [0] * 2 + list(map(int, input().split())) + [0] * 2
    total = 0
    for idx in range(2, n + 2):
        min_floor = float("inf")
        for p in pos:
            min_floor = min(min_floor, buildings[idx] - buildings[idx + p])
        total += min_floor if min_floor >= 0 else 0
    print("#{0} {1}".format(num, total))
