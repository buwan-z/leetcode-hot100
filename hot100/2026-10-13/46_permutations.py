class Solution:
    def permutations(self,nums:list[int])->list[list[int]]:

        ans=[]
        path=[]
        n=len(nums)
        vis=[False]*n
        def dfs(k:int):
            if k==n:
                ans.append(path[:])
                return

            for i in range(n):
                if vis[i]==False:
                    vis[i]=True
                    path.append(nums[i])
                    dfs(k+1)
                    path.pop()
                    vis[i]=False

        dfs(0)
        return ans



        






def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().permutations(nums)
    print(len(ans))
    for l in  ans:
        print(*l) 


if __name__ == "__main__":
    main()