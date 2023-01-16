import collections

class Solution:
    Point = collections.namedtuple('Point','i j')
    def getPoints(self, querie):
        start_i,start_j,end_i,end_j = querie
        points = []
        for i in range(start_i,end_i+1):
            for j in range(start_j,end_j+1):
                points.append(self.Point(i,j))
        return points
            
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        box = [[0 for _ in range(n+1)] for _ in range(n)]
        answer = [[0 for _ in range(n)] for _ in range(n)]
        for querie in queries:
            start_i,start_j,end_i,end_j = querie
            for i in range(start_i,end_i+1):
                box[i][start_j] += 1
                box[i][end_j+1] -= 1
        
        for i in range(n):
            for j in range(n):
                if j == 0:
                    answer[i][j] = box[i][j]
                else:
                    answer[i][j] = box[i][j] + answer[i][j-1]
        return answer