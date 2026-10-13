class Solution:
    def maxProduct(self,nums:list[int])->int:
        # 乘积最大子数组
        # 状态定义 
        # max_product[i] 以nums[i]结尾的子数组乘积的最大值
        # min_product[i] 以nums[i]结尾的子数组乘积的最小值
        n=len(nums)
        max_product=[float("-inf")]*n
        min_product=[float("inf")]*n

        # 状态转移方程
        # max_product[i]=max(max_product[i-1]*nums[i],min_product[i-1]*nums[i],nums[i])
        # min_product[i]=min(max_product[i-1]*nums[i],min_product[i-1]*nums[i],nums[i])

        # 初始化
        max_product[0]=nums[0]
        min_product[0]=nums[0]
        ans=nums[0]

        # 遍历顺序
        for i in range(1,n):
            max_product[i]=max(max_product[i-1]*nums[i],min_product[i-1]*nums[i],nums[i])
            min_product[i]=min(max_product[i-1]*nums[i],min_product[i-1]*nums[i],nums[i])
            ans=max(ans,max_product[i])


        # 手动模拟
        # 2 3 -2 4
        # 2 6 -2 4
        # 2 3 -12 -48

        return ans



def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().maxProduct(nums)
    print(ans)

if __name__=="__main__":
    main()