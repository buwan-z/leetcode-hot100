class Solution:
    def word_search(self,board:list[list[str]],word:str)->bool:
        m,n=len(board),len(board[0])
        vis=[[False]*n for _ in range(m)]

        dirt=[(0,1),(1,0),(0,-1),(-1,0)]
        # 遍历x，y  位置 开始匹配第k个字符
        def dfs(x:int,y:int,k:int)->bool:
            if k==len(word)-1 and board[x][y]==word[k]:
                return True
            if board[x][y]!=word[k]:
                return False

            vis[x][y]=True
            for dx,dy in dirt:
                nx,ny=x+dx,y+dy
                if 0<=nx<=m-1 and 0<=ny<=n-1 and vis[nx][ny]==False:
                    if dfs(nx,ny,k+1)==True:
                        return True
                    else:
                        continue                

            vis[x][y]=False
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False




def main():
    m,n=map(int,input().split())
    board=[list(input().strip()) for _ in  range(m)]
    word=input()
    ans = Solution().word_search(board,word)
    print(str(ans).lower())

if __name__ == "__main__":
    main()