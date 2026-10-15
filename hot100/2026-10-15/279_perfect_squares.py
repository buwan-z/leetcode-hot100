import math
class Solution:
    def perfect_squares(self,n:int)->int:
        # 状态定义
        # dp[i] 整数i 所需要的最少完全平方数
        dp=[float("inf")]*(n+1)

        # 状态转移方程
        # dp[i]=min(dp[i],dp[i-j*j]+1)

        # 初始化
        dp[0]=0
        dp[1]=1
        if n<=1:
            return n
        dp[2]=2

        # 遍历顺序
        # 完全背包
        for i in range(3,n+1):
            for j in range(1,int(pow(i,0.5))+1,1):
                dp[i]=min(dp[i],dp[i-j*j]+1)

        # 手动遍历
        # 1 2 3 4 5 6 7 8 9 10 11 12
        # 1 2 3 2 
        
        return dp[n]


def main():
    n=int(input().strip())
    ans=Solution().perfect_squares(n)
    print(ans)

if __name__ == "__main__":
    main()