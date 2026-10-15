class Solution:
    def move_zeros(self,nums:list[int])->list[int]:
        slow=0
        for fast,num in enumerate(nums):
            if nums[fast]:
                nums[slow]=num
                slow+=1

        for i in range(slow,len(nums)):
            nums[i]=0
        return nums



def main():
    n=int(input())
    nums=list(map(int,input().split()))[:n]
    ans=Solution().move_zeros(nums)
    print(*ans)



if __name__ == "__main__":
    main()