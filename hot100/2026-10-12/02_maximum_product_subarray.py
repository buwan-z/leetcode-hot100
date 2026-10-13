class Solution:
    def maximunSubArray(self,nums:list[int])->int:
        # 状态定义
        # max_array[i] 以nums[i]结尾子数组的最大值
        # min_array[i] 以nums[i]结尾子数组的最小值
        n=len(nums)
        max_array=[float("-inf")]*(n)
        min_array=[float("inf")]*(n)
        # 状态转移方程
        # max_array[i]= max(max_array[i-1]*nums[i],
        #                    min_array[i-1]*nums[i],
        #                    nums[i])

        # min_array[i]= min(max_array[i-1]*nums[i],
        #                    min_array[i-1]*nums[i],
        #                    nums[i])


        # 初始化
        max_array[0]=nums[0]
        min_array[0]=nums[0]

        ans=max_array[0]
        # 遍历顺序
        for i in range(1,n):
            max_array[i]= max(max_array[i-1]*nums[i],
                           min_array[i-1]*nums[i],
                          nums[i]) 
            min_array[i]= min(max_array[i-1]*nums[i],
                           min_array[i-1]*nums[i],
                           nums[i])

            ans=max(ans,max_array[i])

        # 手动模拟

        return ans


def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().maximunSubArray(nums)
    print(ans)

if __name__=="__main__":
    main()