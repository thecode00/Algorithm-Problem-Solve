# https://leetcode.com/problems/utf-8-validation/


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(idx: int, count: int) -> bool:
            for i in range(1, count + 1):
                if idx >= len(data) or data[idx + i] >> 6 != 0b10:
                    return False
            return True  # Vaild UTF-8

        index = 0
        flag = True
        while index < len(data) and flag:
            bits = data[index]
            if bits >> 7 == 0b0:
                index += 1
            elif bits >> 5 == 0b110:
                flag = check(index, 1)
                index += 2
            elif bits >> 4 == 0b1110:
                flag = check(index, 2)
                index += 3
            elif bits >> 3 == 0b11110:
                flag = check(index, 3)
                index += 4
            else:   # If not vaild UTF-8 exist
                return False
        return flag
