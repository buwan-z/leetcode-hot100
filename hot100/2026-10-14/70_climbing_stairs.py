class Solution:
    def climb_stair(self,n:int)->int:
        # 状态定义
        # dp[i] 爬到第i层 有dp[i]种方法

        # 状态转移方程
        # dp[i]=dp[i-1]+dp[i-2]

        # 初始化
        dp=[0]*(n+1)
        dp[1]=1
        if n<=1:
            return 0
        dp[2]=2

        # 遍历顺序
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        # 手动模拟
        # 1 2 3 
        return dp[n]




def main():
    n = int(input())
    ans = Solution().climb_stair(n)
    print(ans)

if __name__ == "__main__":
    main() 