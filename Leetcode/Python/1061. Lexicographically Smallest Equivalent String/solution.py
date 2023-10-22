# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/


class Solution: # Union find
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = dict()

        def find(s: str) -> str:
            if parent[s] != s:
                parent[s] = find(parent[s])
            return parent[s]
        
        def union(s1: str, s2: str) -> None:
            s1, s2 = find(s1), find(s2) # Find parent char
            if s1 > s2:
                parent[s1] = s2
            else:
                parent[s2] = s1
            
        for c1, c2 in zip(s1, s2):
            if c1 not in parent:
                parent[c1] = c1
            if c2 not in parent:
                parent[c2] = c2
            
            union(c1, c2)
        
        result = []
        for char in baseStr:
            if char in parent: # If equivalent character exist convert char
                result.append(find(char))
                continue
            result.append(char)
        return "".join(result)
            

