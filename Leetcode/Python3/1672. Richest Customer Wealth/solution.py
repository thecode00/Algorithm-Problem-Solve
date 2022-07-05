# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for money in accounts:
            answer = max(answer, sum(money))
        return answer
