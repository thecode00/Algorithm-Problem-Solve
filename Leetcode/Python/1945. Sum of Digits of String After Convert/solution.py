# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        offset = ord("a") - 1
        converted = []
        for char in s:
            converted.append(ord(char) - offset)

        result = "".join(map(str, converted))
        for _ in range(k):
            convert_string = str(result)

            total = 0
            for num in convert_string:
                total += int(num)

            result = total

        return result
