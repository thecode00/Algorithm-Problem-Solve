# 1491. Average Salary Excluding the Minimum and Maximum Salary

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        # Exclude max, min value with slice
        return sum(salary[1: -1]) // (len(salary) - 2)
