class Solution:
    def spiral_matrix(self,nums:list[list[int]])->list[int]:
        ans = []
        m,n=len(nums),len(nums[0])
        dirt=[(0,1),(1,0),(0,-1),(-1,0)]
        vis=[[False]*n for _ in range(m)]
        cur_dirt=0
        x,y=0,0
        while len(ans)<m*n:
            vis[x][y]=True
            ans.append(nums[x][y])
            nx=x+dirt[cur_dirt%4][0]
            ny=y+dirt[cur_dirt%4][1]
            if nx<0 or nx>m-1 or ny <0 or ny >n-1 or vis[nx][ny]==True:
                cur_dirt+=1
                nx=x+dirt[cur_dirt%4][0]
                ny=y+dirt[cur_dirt%4][1]
            x,y=nx,ny



            


        return ans  

def main():
    m,n=map(int,input().split())
    nums = [list(map(int,input().split())) for _ in range(m)]
    ans = Solution().spiral_matrix(nums)
    print(ans)


if __name__ == "__main__":
    main()