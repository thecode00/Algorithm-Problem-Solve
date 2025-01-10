# https://leetcode.com/problems/shifting-letters-ii/description

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        length = len(s)
        diff_array = [0] * length

        for start, end, direction in shifts:
            if direction:
                diff_array[start] += 1

                if end + 1 < length:
                    diff_array[end + 1] -= 1
            else:
                diff_array[start] -= 1

                if end + 1 < length:
                    diff_array[end + 1] += 1

        move_count = 0
        result = []

        # In Python, the modulo operation automatically adjusts for negative numbers,
        # ensuring the result always falls within the range of the divisor, so there is no need to handle negatives explicitly.
        for idx in range(length):
            move_count += diff_array[idx]
            shifted_char = chr(
                (ord(s[idx]) - ord("a") + move_count) % 26 + ord("a"))
            result.append(shifted_char)

        return "".join(result)
