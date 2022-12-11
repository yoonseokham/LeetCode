class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        n = len(grid)
        answer = 0
        for i, _ in enumerate(grid[0]):
            answer += max(grid[j][i] for j in range(n))
        return answer