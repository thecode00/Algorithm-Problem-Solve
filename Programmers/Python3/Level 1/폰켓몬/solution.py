# https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    length = len(nums) // 2
    nums = list(set(nums))    # set로 만들어서 중복포켓몬을 없앰
    answer = length if length <= len(nums) else len(nums)
    return answer
