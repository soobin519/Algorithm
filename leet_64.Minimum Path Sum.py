class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid) #행
        m = len(grid[0]) #열 
        
        #dp 정의 - (무조건 오른쪽/아래로만 갈 수 있다. )
        d = [[0]*m for _ in range(n)]
        d[0][0] = grid[0][0]
        for j in range(1,m): #맨 윗줄
            d[0][j] = d[0][j-1]+grid[0][j]
        for i in range(1,n): #맨 왼쪽줄
            d[i][0] = d[i-1][0]+grid[i][0]
        
        for i in range(1,n):
            for j in range(1,m):
                d[i][j] = min(d[i-1][j],d[i][j-1])+grid[i][j]

        return d[n-1][m-1]
