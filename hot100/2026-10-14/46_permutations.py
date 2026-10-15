class Solution:
    def permutations(self,nums:list[int])->list[list[int]]:
        # 排列第k个数
        ans=[]
        path=[]
        n=len(nums)
        vis=[False]*n
        def dfs(k:int):
            if k==n:
                ans.append(path[:])

            for i in range(len(nums)):
                if vis[i]==False:
                    path.append(nums[i])
                    vis[i]=True

                    dfs(k+1)

                    vis[i]=False
                    path.pop()

        dfs(0)
        return ans


            



def main():
    n=input()
    nums = list(map(int,input().split()))
    ans = Solution().permutations(nums)
    print(len(ans))
    for line in ans:
        print(*line)

if __name__ == "__main__":
    main()