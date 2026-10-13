class Solution:
    def maxSubArray(self,nums:list[int])->int:
        # 状态定义
        # dp[i] 以nums[i]结尾的子数组 最大元素和
        
        # 状态转移方程
        # dp[i]=max(dp[i-1]+nums[i],nums[i])

        # 初始化
        n=len(nums)
        dp=[float("-inf")]*n
        dp[0]=nums[0]
        ans=nums[0]

        # 遍历顺序
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            ans=max(ans,dp[i])
            
        # 手动模拟
        # -2 1 -3 4 -1 2 1 -5 4
        # -2 1 -2 4 3 5 6   -1 4

        return ans


def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().maxSubArray(nums)
    print(ans)


if __name__ == "__main__":
    main()