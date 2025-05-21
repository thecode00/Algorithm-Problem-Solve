
n = int(input())

nums = list(map(int, input().split()))

max_length = 1
left = 0

for right in range(1, n):
    if nums[right] > nums[right - 1] * 2:
        left = right

    max_length = max(max_length, right - left + 1)

print(max_length)
