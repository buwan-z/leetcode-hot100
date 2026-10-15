class Solution:
    def product_except_i(self,nums:list[int])->list[int]:
        nums=[1]+nums+[1]
        n=len(nums)
        # 分别表示nums[i] 左边的乘积和0-i-1 右边的乘积和i+1-n-1
        pre_product=[1]*n
        suf_product=[1]*n
        for i in range(1,n-1):
            pre_product[i]=pre_product[i-1]*nums[i-1]
        for i in range(n-2,0,-1):
            suf_product[i]=suf_product[i+1]*nums[i+1]
        ans=[]
        for i in range(1,n-1):
            ans.append(pre_product[i]*suf_product[i])

        return ans


def main():
    # n=int(input().strip())
    n=4
    # nums=list(map(int,input().split()))
    nums=[1,2,3,4]
    ans=Solution().product_except_i(nums)
    print(*ans)

if __name__ == "__main__":
    main()