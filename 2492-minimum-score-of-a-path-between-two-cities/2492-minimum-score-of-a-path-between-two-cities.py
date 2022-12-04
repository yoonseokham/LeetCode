import collections
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(lambda:collections.defaultdict(bool))
        
        parent = [i for i in range(n+1)]
        def parentX(x):
            if parent[x] == x:
                return x
            parent[x] = parentX(parent[x])
            return parent[x]
        
        def connectXY(x,y):
            x = parentX(x)
            y = parentX(y)
            if x == y:
                return True
            elif x > y:
                parent[x] = y
            else:
                parent[y] = x

        
        for start,end,cost in roads:
            connectXY(start,end)
            if graph[start][end]:
                graph[start][end] = min(cost,graph[start][end])
                graph[end][start] = min(cost,graph[end][start])         
            else:
                graph[start][end] = cost
                graph[end][start] = cost
        connected_with_1 = set()
        answer = 10**4+1
        for i in range(1,n+1):
            if parentX(i) == 1:
                connected_with_1.add(i)
        
        for start,dicts in graph.items():
            for end,cost in dicts.items():
                if start in connected_with_1 and end in connected_with_1:
                    answer = min(answer,cost)
        return answer