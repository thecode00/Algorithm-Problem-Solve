# https://www.acmicpc.net/problem/11286

import heapq
import sys

# 첫번째 코드
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(num), num))

# 두번째 코드, 힙을 두개사용한 코드
input = sys.stdin.readline

n = int(input())
pos_heap = []   # 양수만 넣는 힙, 양수는 수가 작을수록 절대값도 작으므로 최소힙으로 사용
nav_heap = []   # 음수만 넣는 힙, 음수는 수가 클수록 절대값도 커지므로 최대힙으로 사용
for _ in range(n):
    num = int(input())
    if num == 0:
        if pos_heap:
            if nav_heap:    # 양수, 음수힙에 둘다 값이 있을때
                if pos_heap[0] < abs(nav_heap[0]):
                    print(heapq.heappop(pos_heap))
                else:   # 절대값이 같을때 작은값을 출력해야하므로 음수 힙에 있는 값을 출력
                    print(-heapq.heappop(nav_heap))
            else:   # 음수힙이 비었을결우
                print(heapq.heappop(pos_heap))
        else:  # 양수힙이 비었을경우
            if nav_heap:
                print(-heapq.heappop(nav_heap))
            else:   # 두 힙이 모두 비었을경우
                print(0)
    else:
        if num > 0:
            heapq.heappush(pos_heap, num)
        else:
            # 최대힙으로 사용하기위해 부호를 바꿔줌 출력할때도 잊지말고 부호를 바꿔서 출력해야함
            heapq.heappush(nav_heap, -num)
