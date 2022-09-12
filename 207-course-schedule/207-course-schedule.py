import collections


class Solution:

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for prerequisite in prerequisites:
            end, start = prerequisite
            graph[start].append(end)

        def isCycle():
            visited = collections.defaultdict(bool)

            def dfsSearch(start):
                isCycle = False

                def dfs(current_node):
                    nonlocal isCycle
                    visited[current_node] = 'visiting'
                    for node in graph[current_node]:
                        if not visited[node]:
                            dfs(node)
                        if visited[node] == 'visiting':
                            isCycle = True
                    visited[current_node] = 'finished'

                dfs(start)
                return isCycle

            for i in range(numCourses):
                if not visited[i]:
                    result = dfsSearch(i)
                    if result:
                        return False
            return True

        return isCycle()