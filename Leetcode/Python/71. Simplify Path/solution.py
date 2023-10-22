# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # Ex. "/home//foo/".split("/") => ['', 'home', '', 'foo', ''] so skip ""
        skip_path = {".", "", ".."}
        for p in path.split("/"):
            if stack and p == "..":
                stack.pop()
            elif p not in skip_path:
                stack.append(p)

        return "/" + "/".join(stack)
