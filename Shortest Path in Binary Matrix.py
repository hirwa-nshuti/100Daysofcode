'''
In an N by N square grid, each cell is either empty (0) 
or blocked (1).

A clear path from top-left to bottom-right has length
 k if and only if it is composed of cells 
C_1, C_2, ..., C_k such that:

    Adjacent cells C_i and C_{i+1} are connected 
    8-directionally (ie., they are different and 
    share an edge or corner)
    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty
     (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from
 top-left to bottom-right.  If such a path does not exist, 
 return -1.
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def getNeighbours(i, j):
            positions = [[-1,-1], [-1,0], [-1,1],[0,-1], [0,1], [1, -1], [1, 0], [1, 1]]            
            for pos in positions:
                i1, j1 = i + pos[0], j + pos[1]                
                if i1 >= 0 and i1 < n and j1 >= 0 and j1 < n and grid[i1][j1] == 0:
                    yield (i1, j1)
                    
        solution = [[999999] * n for _ in range(n)]
        solution[0][0] = 1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        
        h = []
        heapq.heappush(h, (1, (0, 0, 1)))
        while h:
            est, (i, j, sp) = heapq.heappop(h)            
            solution[i][j] = sp
            if i == n - 1 and j == n - 1:
                break
            for i1, j1 in getNeighbours(i, j):
                if solution[i1][j1] > sp + 1:
                    heapq.heappush(h, (sp + 1 + max(n - i1 - 1, n - j1 - 1), (i1, j1, sp + 1)))
                    solution[i1][j1] = solution[i][j] + 1
        
        if solution[n-1][n-1] == 999999:
            return -1
        else:
            return solution[n-1][n-1]  