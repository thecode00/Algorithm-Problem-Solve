# https://leetcode.com/problems/reorder-data-in-log-files/


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        number, alpha = [], []
        for log in logs:
            print(log.split()[1])
            if log.split()[1].isdigit():    # If content starts with number put in number list
                number.append(log)
            else:
                alpha.append(log)
        # Letter-logs are sorted lexicographically by their contents 
        # If their contents are the same, then sort them lexicographically by their identifiers.
        alpha.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return alpha + number
