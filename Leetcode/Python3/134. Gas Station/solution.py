# https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for idx in range(len(gas)):
            if fuel + gas[idx] < cost[idx]:
                fuel = 0
                start = idx + 1
            else:
                fuel += gas[idx] - cost[idx]
        
        return start
