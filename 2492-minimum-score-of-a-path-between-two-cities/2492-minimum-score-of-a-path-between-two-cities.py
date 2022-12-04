import collections


class union_find(object):
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def connectXY(self, x, y):
        x = self.parentX(x)
        y = self.parentX(y)
        if x > y:
            self.parent[x] = y
        if x < y:
            self.parent[y] = x

    def parentX(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.parentX(self.parent[x])
        return self.parent[x]


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(lambda: collections.defaultdict(bool))
        root_info = union_find(n)
        for start, end, cost in roads:
            root_info.connectXY(start, end)
            if graph[start][end]:
                graph[start][end] = min(cost, graph[start][end])
                graph[end][start] = min(cost, graph[end][start])
            else:
                graph[start][end] = cost
                graph[end][start] = cost
        connected_with_1 = set()
        answer = 10**4 + 1
        for i in range(1, n + 1):
            if root_info.parentX(i) == 1:
                connected_with_1.add(i)

        for start, dicts in graph.items():
            for end, cost in dicts.items():
                if start in connected_with_1 and end in connected_with_1:
                    answer = min(answer, cost)
        return answer