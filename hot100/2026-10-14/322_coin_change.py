class Solution:
    def coin_change(self,coins:list[int],target:int)->int:
        # 完全背包问题
        # dp[j] 凑出金币j 最少需要dp[j]硬币
        # 状态转移方程
        # dp[j]=min(dp[j],dp[j-coin]+1)
        

        # 初始化
        dp=[float("inf")]*(target+1)
        dp[0]=0

        # 遍历顺序 先物品再背包 都可以  
        # 内循环 正遍历
        for coin in coins:
            for j in range(coin,target+1):
                dp[j]=min(dp[j],dp[j-coin]+1)
            # print(dp[-1])

        
        # 手动模拟
        #    0 1 2 3 4 5 6 7 8 9 10 11
        # 1  0 1 2 3 4 5 6 7 8 9 10 11
        # 2  0 1 1 2 2 3 3 4 4 5 5 6
        # 5  0 1 1 2 2 1 2 2 3 3 2 3



        return dp[target]


def main():
    n,target=map(int,input().split())
    coins=list(map(int,input().split()))[:n]
    ans=Solution().coin_change(coins,target)
    print(ans)

if __name__ == "__main__":
    main()