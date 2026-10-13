class Solution:
    def longestSubsequence(self,text1:str,text2:str)->int:
        # 状态定义
        # dp[i][j]: text1的前i个元素和text2 的前j个元素 最大公共子序列的长度

        # 状态转移方程
        # if text1[i-1]==text2[j-1] dp[i][j]=dp[i-1][j-1]+1
        # else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        # 初始化
        # dp[i][0]=0
        # dp[0][j]=0
        m,n=len(text1),len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]

        # 遍历循序
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                   dp[i][j]=max(dp[i-1][j],dp[i][j-1])

        # 手动模拟
        #   a c e
        # a 1 1 1
        # b 1 1 1
        # c 1 2 2 
        # d 1 2 2
        # e 1 2 3



        return  dp[m][n]


def main():
    text1=input()
    text2=input()
    ans=Solution().longestSubsequence(text1,text2)
    print(ans)

if __name__ == "__main__":
    main()