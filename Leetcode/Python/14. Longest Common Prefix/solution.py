# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        flag = False  # Checking unmatch string variable
        length = len(strs)
        strs.sort(key=lambda x: len(x))
        for idx in range(len(strs[0])):
            if flag:
                break
            check = strs[0][idx]
            for i in range(1, length):
                if strs[i][idx] != check:  # If string unmatch break loop
                    flag = True
                    break
            else:  # When loop break
                answer += check
        return answer


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        index = 0
        for s in strs[0]:   # Search prefix in smallest size string
            for word in strs:
                if word[index] != s:
                    return strs[0][:index]
            index += 1
        return strs[0][:index]
