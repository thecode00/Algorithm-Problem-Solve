# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:   # Runtime: 55 ms
        command.replace("()", "o")
        command.replace("(al)", "al")
        return command

    def interpret(self, command: str) -> str:   # Runtime: 32 ms
        dict_replace = {"()": "o", "(al)": "al", "G": "G"}
        answer = ""
        temp = ""
        for s in command:
            temp += s
            if temp in dict_replace:
                answer += dict_replace[temp]
                temp = ""
