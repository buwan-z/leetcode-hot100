class Solution:
    def moveZeros(self,nums:list[int])->list[int]:
        # slow 是填写非零位置，fast 遍历
        slow=0
        for fast,num in enumerate(nums):
            if num:
                nums[slow]=num
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0


        return nums

def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().moveZeros(nums)
    print(*ans)


if __name__=="__main__":
    main()