# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)
        path = []

        for start, end in sorted(tickets):
            ticket_dict[start].append(end)

        # print(ticket_dict)

        def dfs(start):
            while ticket_dict[start]:
                dfs(ticket_dict[start].pop(0))
            path.append(start)

        dfs("JFK")
        # dfs append largest lexical order first, so use slice reverse path list
        return path[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)
        path = []

        for start, end in sorted(tickets):
            ticket_dict[start].append(end)

        # print(ticket_dict)

        def dfs(start):
            while ticket_dict[start]:
                dfs(ticket_dict[start].pop())
            path.append(start)

        dfs("JFK")
        # dfs append largest lexical order first, so use slice reverse path list
        return path[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = defaultdict(list)

        for start, end in sorted(tickets):
            ticket_dict[start].append(end)

        route, stack = [], ["JFK"]
        print(stack[-1])
        while stack:
            while ticket_dict[stack[-1]]:
                stack.append(ticket_dict[stack[-1]].pop(0))
            route.append(stack.pop())

        return route[::-1]
