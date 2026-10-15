from collections import deque


class Solution:
    def rotting_orange(self,grid:list[list[int]])->int:
        minutes=0
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        dirt=[(0,1),(1,0),(0,-1),(-1,0)]
        while q and fresh:
            level_n = len(q)
            for _ in  range(level_n):
                x,y=q.popleft()
                for dx,dy in dirt:
                    nx=x+dx
                    ny=y+dy
                    if 0<=nx<=m-1 and 0<=ny<=n-1 and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx,ny))
                        fresh-=1
            minutes+=1
        return minutes if fresh==0 else -1
        
            





def main():
    m,n=map(int,input().split())
    grid=[list(map(int,input().split()))[:n] for _ in range(m)]
    ans = Solution().rotting_orange(grid)
    print(ans)

if __name__ == "__main__":
    main()