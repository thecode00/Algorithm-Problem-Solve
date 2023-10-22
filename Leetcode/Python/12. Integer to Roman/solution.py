# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        unit = 1
        result = []
        while num > 0:
            convert_num = unit * (num % 10)
            if convert_num == 4:
                result.append("IV")
            elif convert_num == 9:
                result.append("IX")
            elif convert_num == 40:
                result.append("XL")
            elif convert_num == 90:
                result.append("XC")
            elif convert_num == 400:
                result.append("CD")
            elif convert_num == 900:
                result.append("CM")
            else:
                s = ""
                for key, val in roman_dict.items():
                    if val > convert_num:
                        continue

                    s += (convert_num // val) * key
                    convert_num %= val
                    if convert_num == 0:
                        break
                result.append(s)

            num //= 10
            unit *= 10
        return "".join(reversed(result))
