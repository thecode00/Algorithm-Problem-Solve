
n = int(input())

carry = 1 if n % 5 != 0 else 0

print((n // 5) + carry)
