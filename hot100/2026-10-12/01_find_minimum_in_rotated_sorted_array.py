
class Solution:
    def findMinNum(self,nums:list[int])->int:
        # 第一个小于等于nums[right]的值
        left,right=0,len(nums)-1
        target=nums[right]
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]<=target:
                right=mid
            else:
                left=mid+1
        return nums[left]


def main():
    n=int(input())
    nums=list(map(int,input().split()))
    ans=Solution().findMinNum(nums)
    print(ans)

if __name__=="__main__":
    main()
        