# https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for num in range(1, n + 1):
            if num % 5 == 0 and num % 3 == 0:
                answer.append("FizzBuzz")
            elif num % 3 == 0:
                answer.append("Fizz")
            elif num % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(num))
        return answer
