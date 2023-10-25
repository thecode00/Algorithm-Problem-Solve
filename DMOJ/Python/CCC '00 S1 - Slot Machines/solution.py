# https://dmoj.ca/problem/ccc00s1

import sys

input = sys.stdin.readline

chips = int(input())
# Input each machine has been played since it last paid.
machines = [int(input()) for _ in range(3)]
machine_index = 0
play_time = 0

while chips:
    machines[machine_index] += 1
    if machine_index == 0 and machines[machine_index] % 35 == 0:
        machines[machine_index] = 0
        chips += 30
    elif machine_index == 1 and machines[machine_index] % 100 == 0:
        machines[machine_index] = 0
        chips += 60
    elif machine_index == 2 and machines[machine_index] % 10 == 0:
        machines[machine_index] = 0
        chips += 9
    play_time += 1
    chips -= 1
    machine_index = (machine_index + 1) % 3

print(f"Martha plays {play_time} times before going broke.")
