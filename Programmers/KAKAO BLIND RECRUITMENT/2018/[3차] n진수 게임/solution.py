# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    # 11진법 이상을 위한 변환 테이블
    convert_table = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    cur = 0
    nums = []

    def convert(num, n):
        """
        입력숫자 num을 n진법으로 변환하여 문자열로 반환하는 함수
        """
        if num == 0:
            return "0"
        result = ""
        while num > 0:
            q, r = divmod(num, n)
            # 나머지가 10이상이라면 변환테이블에서 가져와서 추가하고 그 이하라면 그냥 문자열로 변환하여 추가
            result += convert_table.get(r, str(r))
            num = q

        return result[::-1]

    while len(nums) < t * m:
        changed = convert(cur, n)
        for num in changed:
            nums.append(num)
        cur += 1
    # TODO: 슬라이싱하지않고 크기 조절하여 반환하는법 찾기
    return "".join([nums[idx] for idx in range(p - 1, len(nums), m)])[:t]
