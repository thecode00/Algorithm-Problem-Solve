# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description

class Solution:  # First code
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


class Solution:  # Optimized code
    def getLucky(self, s: str, k: int) -> int:
        offset = ord("a") - 1
        result = 0
        for char in s:
            val = ord(char) - offset
            if val < 10:
                result += val
            else:
                result += (val // 10) + (val % 10)

        k -= 1
        for _ in range(k):
            if result < 10:
                break

            total = 0
            while result > 0:
                total += result % 10
                result //= 10

            result = total

        return result
