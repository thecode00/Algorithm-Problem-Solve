# 최대공약수(GCD), 최소공배수(LCM) 구하기

# 1. 유클리드 호제법
# x와 y의 최대공약수는 y와 z의 최대공약수와 같다
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    return (x * y) // GCD(x, y)
