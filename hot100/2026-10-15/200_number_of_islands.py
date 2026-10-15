class Solution:
    def nums_island(self,grid:list[list[str]])->int:
        m,n=len(grid),len(grid[0])

        dirt=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x:int,y:int)->None:
            grid[x][y]="0"
            for dx,dy in dirt:
                nx,ny=x+dx,y+dy
                if 0<=nx<=m-1 and 0<=ny<=n-1 and grid[nx][ny]=="1":
                    dfs(nx,ny)
            return 


        nums=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    nums+=1

        return nums

def main():
    m,n=map(int,input().split())
    grid=[list(input().strip()) for _ in range(m)]
    ans = Solution().nums_island(grid)
    print(ans)

if __name__ =="__main__":
    main()