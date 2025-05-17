
n = int(input())
nums = input().split()
last_index = {}

for idx, num in enumerate(nums):
    last_index[num] = idx

print(len(last_index))

result = [item[0] for item in sorted(last_index.items(), key=lambda x: x[1])]
print(" ".join(result))
