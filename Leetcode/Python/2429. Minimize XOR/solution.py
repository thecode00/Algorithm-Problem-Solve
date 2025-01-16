# https://leetcode.com/problems/minimize-xor/description

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        diff_bit_count = num1.bit_count() - num2.bit_count()
        answer = num1

        # num1 bits < num2 bits, to minimize XOR remove LSB
        if diff_bit_count > 0:
            fill_index = 0
            while diff_bit_count:
                while (answer & (1 << fill_index)) == 0:
                    fill_index += 1

                answer ^= 1 << fill_index
                diff_bit_count -= 1
        # num1 bits >= num2 bits, num1 XOR num2 = 0, replace a non-1 bit with a 1 bit
        else:
            blank_index = 0
            while diff_bit_count < 0:
                while (answer & 1 << blank_index) != 0:
                    blank_index += 1

                answer |= 1 << blank_index
                diff_bit_count += 1

        return answer
