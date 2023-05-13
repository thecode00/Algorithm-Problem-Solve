# Vector sum
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result  = []
for s1, s2 in zip(vector1, vector2):
    result.append(s1 + s2)

print(result)   # [5, 7, 9]

# Vector sub
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
result  = []
for s1, s2 in zip(vector1, vector2):
    result.append(s1 - s2)

print(result)   # [-3, -3, -3]

# Scalar multipulication
scalar = 3
vector1 = [1, 2, 3]
result = []

for idx in range(len(vector1)):
    result.append(scalar * vector1[idx])

print(result)   # [3, 6, 9]

